"""
AI Code Review Script — Enterprise Grade (Cohere version)
---------------------------------------------------------
Полностью исправленный, безопасный и бесплатный вариант через Cohere API.
Автор: Senior Software Engineer (ChatGPT)
"""
import os
import json
import time
import argparse
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from dotenv import load_dotenv
from github import Github
import cohere
from tqdm import tqdm

# ========================================================================
# ЛОГИРОВАНИЕ
# ========================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("AIReview")

# ========================================================================
# ЗАГРУЗКА ОКРУЖЕНИЯ
# ========================================================================
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY is missing in environment")

co = cohere.Client(COHERE_API_KEY)

# ========================================================================
# CLI ПАРАМЕТРЫ
# ========================================================================
parser = argparse.ArgumentParser(description="AI Code Review via Cohere LLM")
parser.add_argument("--project_dir", default=".", help="Path to project")
parser.add_argument("--extensions", nargs="+",
                    default=[".php", ".js", ".jsx", ".vue", ".ts", ".tsx", ".html", ".css", ".py"],
                    help="Extensions to review")
parser.add_argument("--exclude_dirs", nargs="+",
                    default=[".git", "node_modules", "vendor", "venv"],
                    help="Directories to exclude")
parser.add_argument("--max_tokens", type=int, default=4000)
args = parser.parse_args()

PROJECT_DIR = Path(args.project_dir).resolve()
EXTENSIONS = tuple(args.extensions)
EXCLUDE_DIRS = set(args.exclude_dirs)
MAX_CODE_LENGTH = args.max_tokens

# ========================================================================
# GITHUB PR CONNECT
# ========================================================================
github_pr = None

def load_pr():
    global github_pr
    if not GITHUB_TOKEN or not GITHUB_EVENT_PATH:
        logger.warning("GitHub PR comments disabled")
        return

    try:
        with open(GITHUB_EVENT_PATH, "r") as f:
            event = json.load(f)
    except Exception as e:
        logger.error(f"Cannot read GITHUB_EVENT_PATH: {e}")
        return

    pr_number = event.get("pull_request", {}).get("number")
    if not pr_number:
        logger.warning("Not a PR event — skipping PR comments")
        return

    try:
        gh = Github(GITHUB_TOKEN)
        repo = gh.get_repo(GITHUB_REPOSITORY)
        github_pr = repo.get_pull(pr_number)
        logger.info(f"Connected to PR #{pr_number}")
    except Exception as e:
        logger.error(f"GitHub connection failed: {e}")

# ========================================================================
# FILE SCANNING
# ========================================================================
def get_code_files(root: Path):
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(ex in path.parts for ex in EXCLUDE_DIRS):
            continue
        files.append(str(path))
    return files

def read_file(path: str):
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except:
        return ""

# ========================================================================
# AI REVIEW
# ========================================================================
def review_code(path: str, content: str) -> str:
    content = content[:MAX_CODE_LENGTH]
    prompt = f"""
Ты — опытный Senior Software Engineer и Tech Lead.
Проанализируй код файла **{path}** строго по существу.

Код:
---------------------
{content}
---------------------

Ответь структурированно:
- 🧠 Общая оценка
- ⚠️ Проблемы и замечания
- 💡 Рекомендации по улучшению
- 🔒 Безопасность
- 🚀 Оптимизация и производительность
- ✨ Плюсы кода
"""
    try:
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=500,
            temperature=0
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"⚠️ Cohere API error: {e}"

# ========================================================================
# GITHUB COMMENT
# ========================================================================
def post_comment(path: str, review: str):
    if not github_pr:
        return
    try:
        github_pr.create_issue_comment(
            f"### 🤖 AI Review — `{path}`\n\n{review[:65000]}"
        )
        logger.info(f"💬 Comment added for {path}")
        time.sleep(0.5)
    except Exception as e:
        logger.error(f"❌ Failed to comment PR for {path}: {e}")

# ========================================================================
# MAIN
# ========================================================================
def main():
    load_pr()
    logger.info("Scanning files...")
    files = get_code_files(PROJECT_DIR)

    if not files:
        logger.warning("No files found")
        return

    logger.info(f"Found {len(files)} code files")
    all_reviews_text = ""

    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(read_file, f): f for f in files}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Reviewing"):
            fpath = futures[future]
            code = future.result()
            review = "⚠️ Cannot read file" if not code else review_code(fpath, code)

            all_reviews_text += f"\n--- {fpath} ---\n{review}\n"
            post_comment(fpath, review)

    if GITHUB_TOKEN and GITHUB_REPOSITORY:
        try:
            gh = Github(GITHUB_TOKEN)
            repo = gh.get_repo(GITHUB_REPOSITORY)
            issue_title = "🤖 Full AI Code Review"
            issue_body = all_reviews_text[:65000]
            repo.create_issue(title=issue_title, body=issue_body)
            logger.info("✅ GitHub Issue created with full AI review")
        except Exception as e:
            logger.error(f"❌ Failed to create GitHub Issue: {e}")

    logger.info("✅ AI Code Review completed for all files")

if __name__ == "__main__":
    main()
