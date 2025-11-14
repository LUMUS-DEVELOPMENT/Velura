"""
AI Code Review Script — Enterprise Grade (Cohere, robust)
---------------------------------------------------------
Использует Cohere Chat API для ревью кода, публикует per-file PR comments
и создаёт единый Issue с полным обзором. Безопасные retries, throttling.
"""

import os
import json
import time
import argparse
import logging
import random
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

from dotenv import load_dotenv
from github import Github
import cohere
from tqdm import tqdm

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

# Cohere client
co = cohere.Client(COHERE_API_KEY)

# -------------------------
# CLI
# -------------------------
parser = argparse.ArgumentParser(description="AI Code Review via Cohere Chat")
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
parser.add_argument("--max_tokens", type=int, default=1500, help="Max tokens for model response")
parser.add_argument("--max_workers", type=int, default=1, help="Parallel file readers / reviewers")
parser.add_argument("--output", type=str, help="Write full aggregated results to this file")
parser.add_argument("--model", type=str, default="command-light", help="Cohere chat model to use")
args = parser.parse_args()

PROJECT_DIR = Path(args.project_dir).resolve()
EXTENSIONS = tuple(args.extensions)
EXCLUDE_DIRS = set(args.exclude_dirs)
MAX_CODE_LENGTH = args.max_tokens
MAX_WORKERS = max(1, args.max_workers)
MODEL = args.model

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
def get_code_files(root: Path):
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        # skip if any part equals excluded dir
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
# Cohere chat with retries/backoff
# -------------------------
def cohere_chat_with_retries(messages, model: str, max_tokens: int, max_retries: int = 5, initial_backoff: float = 1.0) -> str:
    """
    Calls co.chat with exponential backoff on 429/5xx errors.
    Returns response text on success or raises last exception.
    """
    attempt = 0
    backoff = initial_backoff
    while True:
        attempt += 1
        try:
            # Newer Cohere chat endpoint: co.chat(...)
            response = co.chat(model=model, messages=messages, max_output_tokens=max_tokens, temperature=0)
            # response.text is a convenient representation in many SDK versions
            # Fallback: try to extract text
            if hasattr(response, "text") and response.text:
                return response.text.strip()
            # older/newer shapes: try message/outputs
            if hasattr(response, "message") and getattr(response, "message"):
                msg = response.message
                if isinstance(msg, dict):
                    # try common keys
                    for k in ("content", "text"):
                        if k in msg:
                            return msg[k].strip()
                return str(msg)
            # fallback to string conversion
            return str(response).strip()
        except Exception as e:
            # inspect error string for retryable codes
            err_str = str(e).lower()
            if attempt >= max_retries:
                logger.error("Cohere chat failed after %d attempts: %s", attempt, e)
                raise
            # retry on rate limit / server errors
            if "429" in err_str or "too many requests" in err_str or "500" in err_str or "503" in err_str or "server error" in err_str:
                sleep_for = backoff + random.random() * 0.5
                logger.warning("Cohere API transient error (attempt %d): %s — backing off %.1fs", attempt, e, sleep_for)
                time.sleep(sleep_for)
                backoff *= 2
                continue
            else:
                # non-retryable
                logger.error("Cohere API non-retryable error: %s", e)
                raise


# -------------------------
# AI review logic
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
    snippet = content[: 100_000]

    body = f"Ты — опытный Senior Software Engineer и Tech Lead. Проанализируй код файла  Файл: {path}\n\nКод:\n---------------------\n{snippet}\n---------------------"
    prompt = PROMPT_HEADER + body + PROMPT_FOOTER

    messages = [{"role": "user", "content": prompt}]
    try:
        return cohere_chat_with_retries(messages, model=MODEL, max_tokens=MAX_CODE_LENGTH)
    except Exception as e:
        logger.error("Review failed for %s: %s", path, e)
        return f"⚠️ Cohere API error: {e}"


# -------------------------
# GitHub posting helpers
# -------------------------
def post_pr_comment(path: str, review_text: str):
    if github_pr is None:
        logger.debug("No github_pr loaded, skipping PR comment for %s", path)
        return
    try:
        body = f"### 🤖 AI Review — `{path}`\n\n{review_text[:65000]}"
        github_pr.create_issue_comment(body)
        logger.info("Posted PR comment for %s", path)
        # minimal delay to reduce risk of rate-limits
        time.sleep(0.6)
    except Exception as e:
        logger.error("Failed posting PR comment for %s: %s", path, e)


# -------------------------
# Main
# -------------------------
def main():
    logger.info("Starting AI Code Review...")
    load_pr()

    logger.info("Scanning project dir: %s", PROJECT_DIR)
    files = get_code_files(PROJECT_DIR)
    if not files:
        logger.warning("No files found for analysis.")
        return

    logger.info("Found %d files to review", len(files))

    results = []
    # Use ThreadPoolExecutor only for file reading; limit API parallelism via semaphores would be better,
    # but we keep MAX_WORKERS low to avoid rate limits.
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(read_file, f): f for f in files}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Reviewing"):
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
            # Post individual PR comment if PR is available
            post_pr_comment(fpath, review)

    # Aggregate results
    aggregated = []
    for path, review in results:
        aggregated.append(f"\n--- {path} ---\n{review}\n")
    aggregated_text = "".join(aggregated)

    # Create GitHub Issue with full review if repo/token available
    if GITHUB_TOKEN and GITHUB_REPOSITORY:
        try:
            gh = Github(GITHUB_TOKEN)
            repo = gh.get_repo(GITHUB_REPOSITORY)
            issue_title = "🤖 Full AI Code Review"
            # Truncate to safe size for GitHub issue body
            issue_body = aggregated_text[:65000] if len(aggregated_text) > 0 else "No review content generated."
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
