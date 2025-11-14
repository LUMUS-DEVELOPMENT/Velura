#!/usr/bin/env python3
"""
AI Code Review Script — Cohere-compatible (robust)
-------------------------------------------------
Supports multiple Cohere SDK shapes, retries/backoff, PR comments and Issue creation.
"""

import os
import json
import time
import argparse
import logging
import random
import inspect
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from github import Github

# Try to import Cohere Client in a couple of ways to maximize compatibility
try:
    # modern: from cohere import Client
    from cohere import Client as CohereClient
    _COHERE_IMPORTED = "cohere.Client"
except Exception:
    try:
        # older package style: import cohere
        import cohere as _cohere_pkg  # type: ignore

        CohereClient = getattr(_cohere_pkg, "Client", None)
        _COHERE_IMPORTED = "cohere (fallback)"
    except Exception:
        CohereClient = None
        _COHERE_IMPORTED = None

# -------------------------
# Logging
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("AIReview")

# -------------------------
# Load env
# -------------------------
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY is missing in environment")

if CohereClient is None:
    raise ImportError("Cohere client could not be imported. Install 'cohere' package.")

# create client
try:
    co = CohereClient(COHERE_API_KEY)
except TypeError:
    # Some older versions expect keyword arg name 'api_key'
    co = CohereClient(api_key=COHERE_API_KEY)  # type: ignore

# -------------------------
# CLI
# -------------------------
parser = argparse.ArgumentParser(description="AI Code Review via Cohere Chat (robust)")
parser.add_argument("--project_dir", default=".", help="Path to project")
parser.add_argument(
    "--extensions",
    nargs="+",
    default=[".php", ".js", ".jsx", ".vue", ".ts", ".tsx", ".html", ".css", ".py"],
    help="Extensions to review",
)
parser.add_argument(
    "--exclude_dirs",
    nargs="+",
    default=[".git", "node_modules", "vendor", "venv"],
    help="Directories to exclude",
)
parser.add_argument("--max_tokens", type=int, default=1200, help="Max tokens for model response")
parser.add_argument("--max_workers", type=int, default=1, help="Number of parallel file processing workers (keep low to avoid rate limits)")
parser.add_argument("--output", type=str, help="Write full aggregated results to this file")
parser.add_argument("--model", type=str, default="command-light", help="Cohere model name (e.g. command-light, command-r)")
parser.add_argument("--chunk_size_chars", type=int, default=100000, help="Max characters of file to send to model")
args = parser.parse_args()

PROJECT_DIR = Path(args.project_dir).resolve()
EXTENSIONS = tuple(args.extensions)
EXCLUDE_DIRS = set(args.exclude_dirs)
MAX_CODE_TOKENS = args.max_tokens
MAX_WORKERS = max(1, args.max_workers)
MODEL = args.model
CHUNK_SIZE_CHARS = args.chunk_size_chars

# -------------------------
# GitHub PR helper
# -------------------------
github_pr = None


def load_pr() -> None:
    """Load PR object from GITHUB_EVENT_PATH if available."""
    global github_pr
    if not GITHUB_TOKEN or not GITHUB_EVENT_PATH or not GITHUB_REPOSITORY:
        logger.warning("GitHub PR comments disabled (missing token/event_path/repo).")
        return

    try:
        with open(GITHUB_EVENT_PATH, "r", encoding="utf-8") as f:
            event = json.load(f)
    except Exception as e:
        logger.error("Cannot read GITHUB_EVENT_PATH: %s", e)
        return

    pr_number = event.get("pull_request", {}).get("number")
    if not isinstance(pr_number, int):
        logger.warning("Not a pull_request event (PR number missing). Skipping PR comments.")
        return

    try:
        gh = Github(GITHUB_TOKEN)
        repo = gh.get_repo(GITHUB_REPOSITORY)
        github_pr = repo.get_pull(pr_number)
        logger.info("Connected to PR #%s", pr_number)
    except Exception as e:
        logger.error("GitHub connection failed: %s", e)
        github_pr = None


# -------------------------
# Files utilities
# -------------------------
def get_code_files(root: Path) -> List[str]:
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        files.append(str(path))
    return sorted(files)


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        logger.warning("Unable to read %s: %s", path, e)
        return ""


# -------------------------
# Cohere call wrapper (robust)
# -------------------------
def _call_cohere_chat(messages: List[Dict[str, str]], model: str, max_output_tokens: int) -> str:
    """
    Try several invocation patterns for co.chat / co.generate, and extract text robustly.
    Raises last exception on fatal error.
    """
    # Candidate call patterns with kwargs to try (ordered)
    patterns = [
        {"method": "chat", "kwargs": {"model": model, "messages": messages, "max_output_tokens": max_output_tokens}},
        {"method": "chat", "kwargs": {"model": model, "messages": messages, "max_tokens": max_output_tokens}},
        {"method": "chat", "kwargs": {"model": model, "inputs": messages[0]["content"], "max_output_tokens": max_output_tokens}},
        {"method": "generate", "kwargs": {"model": model, "prompt": messages[0]["content"], "max_tokens": max_output_tokens}},
        {"method": "generate", "kwargs": {"model": model, "prompt": messages[0]["content"], "max_output_tokens": max_output_tokens}},
    ]

    last_exc: Optional[Exception] = None
    for p in patterns:
        method_name = p["method"]
        kwargs = p["kwargs"]
        if not hasattr(co, method_name):
            continue
        method = getattr(co, method_name)
        try:
            # Inspect signature to avoid unexpected kwargs where possible
            sig = None
            try:
                sig = inspect.signature(method)
            except Exception:
                sig = None
            if sig:
                # filter kwargs to signature
                filtered_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
            else:
                filtered_kwargs = kwargs
            resp = method(**filtered_kwargs)
            text = _extract_text_from_cohere_response(resp)
            if text is not None:
                return text
            # fallback: string conversion
            return str(resp)
        except TypeError as te:
            # likely unexpected kwarg; try next pattern
            last_exc = te
            continue
        except Exception as e:
            # For 429/5xx we want caller to handle retry, so raise
            last_exc = e
            raise
    # If we exhausted patterns, raise the last exception
    if last_exc:
        raise last_exc
    raise RuntimeError("No suitable cohere method found.")


def _extract_text_from_cohere_response(resp: Any) -> Optional[str]:
    """
    Extract textual content from various possible response shapes.
    Return None if can't find text.
    """
    try:
        # prefer .text
        if hasattr(resp, "text") and isinstance(resp.text, str) and resp.text.strip():
            return resp.text.strip()
        # some versions: .message or .generations
        if hasattr(resp, "message") and resp.message:
            msg = resp.message
            # message might be dict-like
            if isinstance(msg, dict):
                for k in ("content", "text", "message"):
                    v = msg.get(k)
                    if isinstance(v, str) and v.strip():
                        return v.strip()
                # message might have nested 'content' list
                if "content" in msg and isinstance(msg["content"], list) and msg["content"]:
                    first = msg["content"][0]
                    if isinstance(first, dict):
                        for k in ("text", "parts", "content"):
                            if k in first and isinstance(first[k], str) and first[k].strip():
                                return first[k].strip()
            else:
                return str(msg).strip()
        if hasattr(resp, "generations") and resp.generations:
            gens = resp.generations
            # gens can be a list of objects with .text
            try:
                first = gens[0]
                if hasattr(first, "text"):
                    return first.text.strip()
                if isinstance(first, dict):
                    for k in ("text", "content"):
                        if k in first and isinstance(first[k], str) and first[k].strip():
                            return first[k].strip()
            except Exception:
                pass
        # some have .outputs
        if hasattr(resp, "outputs") and resp.outputs:
            outs = resp.outputs
            try:
                first = outs[0]
                if isinstance(first, dict):
                    for k in ("content", "text"):
                        if k in first and isinstance(first[k], str) and first[k].strip():
                            return first[k].strip()
            except Exception:
                pass
        # try to convert to dict
        if hasattr(resp, "to_dict"):
            d = resp.to_dict()
            # search for first string in dict values
            def walk(v):
                if isinstance(v, str) and v.strip():
                    return v.strip()
                if isinstance(v, dict):
                    for val in v.values():
                        r = walk(val)
                        if r:
                            return r
                if isinstance(v, list):
                    for item in v:
                        r = walk(item)
                        if r:
                            return r
                return None
            found = walk(d)
            if found:
                return found
    except Exception:
        pass
    return None


# -------------------------
# Cohere chat with retries/backoff (public)
# -------------------------
def cohere_chat_with_retries(messages: List[Dict[str, str]], model: str, max_tokens: int, max_retries: int = 5) -> str:
    attempt = 0
    backoff = 1.0
    while True:
        attempt += 1
        try:
            return _call_cohere_chat(messages=messages, model=model, max_output_tokens=max_tokens)
        except Exception as e:
            err_str = str(e).lower()
            # decide whether to retry
            if attempt >= max_retries:
                logger.error("Cohere call failed after %d attempts: %s", attempt, e)
                raise
            # retry on rate limit or 5xx-like messages
            if "429" in err_str or "too many requests" in err_str or "server error" in err_str or "timeout" in err_str or "503" in err_str or "500" in err_str:
                sleep_for = backoff + random.random() * 0.5
                logger.warning("Cohere transient error (attempt %d): %s — sleeping %.1fs", attempt, e, sleep_for)
                time.sleep(sleep_for)
                backoff *= 2
                continue
            # non-retryable: re-raise
            logger.error("Cohere non-retryable error: %s", e)
            raise


# -------------------------
# Prompt & review logic
# -------------------------
PROMPT_HEADER = (
    "Ты — опытный Senior Software Engineer и Tech Lead с глубоким знанием лучших практик разработки, "
    "архитектуры и безопасности. Проведи жёсткое и детальное ревью кода, как это делает старший инженер.\n\n"
)

PROMPT_FOOTER = (
    "\n\nОтветь структурированно в секциях:\n"
    "- 🧠 Общая оценка\n"
    "- ⚠️ Проблемы и замечания\n"
    "- 💡 Рекомендации по улучшению\n"
    "- 🔒 Безопасность\n"
    "- 🚀 Оптимизация и производительность\n"
    "- ✨ Плюсы кода\n"
    "Пиши коротко, профессионально, без фраз вроде 'Я думаю' или 'Возможно'."
)


def review_code(path: str, content: str) -> str:
    snippet = content[:CHUNK_SIZE_CHARS]
    body = f"Файл: {path}\n\nКод:\n---------------------\n{snippet}\n---------------------"
    prompt = PROMPT_HEADER + body + PROMPT_FOOTER
    messages = [{"role": "user", "content": prompt}]
    try:
        review_text = cohere_chat_with_retries(messages=messages, model=MODEL, max_tokens=MAX_CODE_TOKENS)
        return review_text
    except Exception as e:
        logger.error("Review failed for %s: %s", path, e)
        return f"⚠️ Cohere API error: {e}"


# -------------------------
# GitHub posting helpers
# -------------------------
def post_pr_comment(path: str, review_text: str) -> None:
    if github_pr is None:
        logger.debug("No github_pr loaded, skipping PR comment for %s", path)
        return
    try:
        body = f"### 🤖 AI Review — `{path}`\n\n{review_text[:65000]}"
        github_pr.create_issue_comment(body)
        logger.info("Posted PR comment for %s", path)
        time.sleep(0.6)
    except Exception as e:
        logger.error("Failed posting PR comment for %s: %s", path, e)


# -------------------------
# Main
# -------------------------
def main() -> None:
    logger.info("Starting AI Code Review (Cohere import: %s)...", _COHERE_IMPORTED)
    load_pr()

    logger.info("Scanning project dir: %s", PROJECT_DIR)
    files = get_code_files(PROJECT_DIR)
    if not files:
        logger.warning("No files found for analysis.")
        return

    logger.info("Found %d files to review", len(files))

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(read_file, f): f for f in files}
        for future in as_completed(futures):
            fpath = futures[future]
            try:
                code = future.result()
            except Exception as e:
                logger.error("Failed to read file %s: %s", fpath, e)
                code = ""

            if not code:
                review = "⚠️ Cannot read file or file is empty"
                logger.warning("%s: %s", review, fpath)
            else:
                logger.info("Reviewing %s", fpath)
                review = review_code(fpath, code)

            results.append((fpath, review))
            post_pr_comment(fpath, review)

    # Aggregate results
    aggregated = []
    for path, review in results:
        aggregated.append(f"\n--- {path} ---\n{review}\n")
    aggregated_text = "".join(aggregated)

    # Create GitHub Issue with full review if possible
    if GITHUB_TOKEN and GITHUB_REPOSITORY:
        try:
            gh = Github(GITHUB_TOKEN)
            repo = gh.get_repo(GITHUB_REPOSITORY)
            issue_title = "🤖 Full AI Code Review"
            issue_body = aggregated_text[:65000] if aggregated_text else "No review content generated."
            repo.create_issue(title=issue_title, body=issue_body)
            logger.info("Created GitHub Issue with full review")
        except Exception as e:
            logger.error("Failed to create GitHub Issue: %s", e)
    else:
        logger.info("Skipping Issue creation (missing GITHUB_TOKEN or GITHUB_REPOSITORY)")

    # Save output locally if requested
    if args.output:
        try:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(aggregated_text, encoding="utf-8")
            logger.info("Results saved to %s", args.output)
        except Exception as e:
            logger.error("Failed to write output file: %s", e)

    logger.info("AI Code Review completed.")


if __name__ == "__main__":
    main()
