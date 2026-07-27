import os
import json
import glob
import yaml
import pickle
import logging
import re
from pathlib import Path
from typing import List, Dict

from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = ["_posts", "_pages", "learning", "notes"]
EXCLUDE_DIRS = ["_site", ".git", "vendor", ".bundle", "node_modules", "server"]
INDEX_DIR = ROOT / ".opencode"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def load_markdown_files() -> List[Dict]:
    files = []
    for content_dir in CONTENT_DIRS:
        search_path = ROOT / content_dir / "**/*.md"
        for fp in glob.glob(str(search_path), recursive=True):
            fp = Path(fp)
            if any(excl in fp.parts for excl in EXCLUDE_DIRS):
                continue
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                meta = {}
                body = content
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        try:
                            meta = yaml.safe_load(parts[1]) or {}
                        except yaml.YAMLError:
                            meta = {}
                        body = parts[2].strip()
                rel_path = fp.relative_to(ROOT)
                files.append({
                    "path": str(rel_path),
                    "title": meta.get("title", fp.stem),
                    "categories": meta.get("categories", meta.get("category", "")),
                    "tags": meta.get("tags", []),
                    "body": body,
                })
            except Exception as e:
                logger.warning(f"Error reading {fp}: {e}")
    logger.info(f"Loaded {len(files)} markdown files")
    return files


def chunk_text(text: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP) -> List[str]:
    words = re.split(r"\s+", text)
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start = end - overlap
        if start < 0:
            start = 0
    return chunks if chunks else [text]


def build_index():
    logger.info("Loading markdown files...")
    files = load_markdown_files()

    all_chunks = []
    all_metadatas = []

    for doc in files:
        chunks = chunk_text(doc["body"])
        tag_str = ", ".join(doc["tags"]) if isinstance(doc["tags"], list) else str(doc["tags"] or "")
        cat_str = doc["categories"] if isinstance(doc["categories"], str) else ", ".join(doc["categories"]) if isinstance(doc["categories"], list) else ""
        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadatas.append({
                "path": doc["path"],
                "title": doc["title"],
                "categories": cat_str,
                "tags": tag_str,
            })

    logger.info(f"Building TF-IDF index ({len(all_chunks)} chunks)...")
    vectorizer = TfidfVectorizer(
        max_features=50000,
        stop_words=["的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有", "看", "好", "自己", "这"],
        token_pattern=r"(?u)\b\w+\b",
    )
    tfidf_matrix = vectorizer.fit_transform(all_chunks)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_DIR / "vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open(INDEX_DIR / "tfidf_matrix.pkl", "wb") as f:
        pickle.dump(tfidf_matrix, f)
    with open(INDEX_DIR / "chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)
    with open(INDEX_DIR / "metadatas.pkl", "wb") as f:
        pickle.dump(all_metadatas, f)

    logger.info(f"Index complete: {len(all_chunks)} chunks")
    return len(all_chunks)


if __name__ == "__main__":
    count = build_index()
    print(f"Successfully indexed {count} chunks")
