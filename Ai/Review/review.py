#!/usr/bin/env python3
"""
AI Code Review Script — Cohere Compatibility via OpenAI SDK
-----------------------------------------------------------
Uses OpenAI SDK with Cohere Compatibility API.
Supports retries, PR comments, Issue creation.
"""

import os
import json
import time
import argparse
import logging
import random
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

from dotenv import load_dotenv
from github import Github
from openai import OpenAI

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

# OpenAI client pointing to Cohere Compatibility API
client = OpenAI(base_url="https://api.cohere.ai/compatibility/v1", api_key=COHERE_API_KEY)

# -------------------------
# CLI
# -------------------------
parser = argparse.ArgumentParser(description="AI Code Review via Cohere Compatibility API")
parser.add_argument("--project_dir", default=".", help="Path to project")
parser.add_argument(
    "--extensions",
    nargs="+",
    default=[".php", ".js", ".jsx", ".vue", ".ts", ".tsx", ".html", ".css", ".py"],
    help="Extensions to review",
)
parser.add_argument("--max_tokens", type=int, default=1200, help="Max tokens for model response")
parser.add_argument("--max_workers", type=int, default=1, help="Number of parallel file processing workers")
parser.add_argument("--output", type=str, help="Write full aggregated results to this file")
parser.add_argument("--model", type=str, default="command-a-03-2025", help="Cohere chat model via Compatibility API")
parser.add_argument("--chunk_size_chars", type=int, default=100000, help="Max characters of file to send to model")
args = parser.parse_args()

PROJECT_DIR = Path(args.project_dir).resolve()
EXTENSIONS = tuple(args.extensions)
MAX_WORKERS = max(1, args.max_workers)
MAX_CODE_TOKENS = args.max_tokens
MODEL = args.model
CHUNK_SIZE_CHARS = args.chunk_size_chars

# -------------------------
# GitHub PR helper
# -------------------------
github_pr = None

def load_pr() -> None:
    global github_pr
    if not GITHUB_TOKEN or not GITHUB_EVENT_PATH or not GITHUB_REPOSITORY:
        logger.warning("GitHub PR comments disabled (missing token/event_path/repo).")
        return
    try:
        with open(GITHUB_EVENT_PATH, "r", encoding="utf-8") as f:
            event = json.load(f)
        pr_number = event.get("pull_request", {}).get("number")
        if not isinstance(pr_number, int):
            logger.warning("Not a pull_request event (PR number missing). Skipping PR comments.")
            return
        gh = Github(GITHUB_TOKEN)
        repo = gh.get_repo(GITHUB_REPOSITORY)
        github_pr = repo.get_pull(pr_number)
        logger.info("Connected to PR #%s", pr_number)
    except Exception as e:
        logger.error("GitHub connection failed: %s", e)
        github_pr = None

# -------------------------
# File utilities
# -------------------------
def get_code_files(root: Path) -> List[str]:
    files = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in EXTENSIONS:
            files.append(str(path))
    return sorted(files)

def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        logger.warning("Unable to read %s: %s", path, e)
        return ""

# -------------------------
# Cohere Compatibility chat with retries
# -------------------------
def cohere_chat_with_retries(messages: List[Dict[str, str]], model: str, max_tokens: int, max_retries: int = 5) -> str:
    attempt = 0
    backoff = 1.0
    while True:
        attempt += 1
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens
            )
            return resp.choices[0].message.content
        except Exception as e:
            err_str = str(e).lower()
            if attempt >= max_retries:
                logger.error("Cohere call failed after %d attempts: %s", attempt, e)
                raise
            if any(x in err_str for x in ["429", "too many requests", "503", "500", "timeout"]):
                sleep_for = backoff + random.random() * 0.5
                logger.warning("Transient error (attempt %d): %s — sleeping %.1fs", attempt, e, sleep_for)
                time.sleep(sleep_for)
                backoff *= 2
                continue
            raise

# -------------------------
# Review logic
# -------------------------
PROMPT_HEADER = (
    "Ты — опытный Senior Software Engineer и Tech Lead с глубоким знанием лучших практик разработки, "
    "архитектуры и безопасности. Проведи жёсткое и детальное ревью кода.\n\n"
)

PROMPT_FOOTER = (
    "\n\nОтветь структурированно в секциях:\n"
    "- 🧠 Общая оценка\n"
    "- ⚠️ Проблемы и замечания\n"
    "- 💡 Рекомендации по улучшению\n"
    "- 🔒 Безопасность\n"
    "- 🚀 Оптимизация и производительность\n"
    "- ✨ Плюсы кода\n"
    "Пиши коротко и профессионально."
)

def review_code(path: str, content: str) -> str:
    snippet = content[:CHUNK_SIZE_CHARS]
    body = f"Файл: {path}\n\nКод:\n---------------------\n{snippet}\n---------------------"
    prompt = PROMPT_HEADER + body + PROMPT_FOOTER
    messages = [{"role": "user", "content": prompt}]
    try:
        return cohere_chat_with_retries(messages, MODEL, MAX_CODE_TOKENS)
    except Exception as e:
        logger.error("Review failed for %s: %s", path, e)
        return f"⚠️ API error: {e}"

# -------------------------
# GitHub helpers
# -------------------------
def post_pr_comment(path: str, review_text: str) -> None:
    if github_pr is None:
        return
    try:
        github_pr.create_issue_comment(f"### 🤖 AI Review — `{path}`\n\n{review_text[:65000]}")
        time.sleep(0.6)
    except Exception as e:
        logger.error("Failed posting PR comment for %s: %s", path, e)

# -------------------------
# Main
# -------------------------
def main() -> None:
    logger.info("Starting AI Code Review via Cohere Compatibility API...")
    load_pr()

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
            code = future.result()
            review = review_code(fpath, code) if code else "⚠️ Cannot read file or empty"
            results.append((fpath, review))
            post_pr_comment(fpath, review)

    aggregated_text = "\n".join(f"\n--- {p} ---\n{r}\n" for p, r in results)

    if GITHUB_TOKEN and GITHUB_REPOSITORY:
        try:
            gh = Github(GITHUB_TOKEN)
            repo = gh.get_repo(GITHUB_REPOSITORY)
            repo.create_issue(title="🤖 Full AI Code Review", body=aggregated_text[:65000])
        except Exception as e:
            logger.error("Failed to create GitHub Issue: %s", e)

    if args.output:
        try:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(aggregated_text, encoding="utf-8")
        except Exception as e:
            logger.error("Failed to write output file: %s", e)

    logger.info("AI Code Review completed.")

if __name__ == "__main__":
    main()
