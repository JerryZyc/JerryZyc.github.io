import os
import pickle
import logging
from pathlib import Path
from typing import List, Optional

import numpy as np
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = ROOT / ".opencode"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

app = FastAPI(title="Site Chat API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_vectorizer = None
_tfidf_matrix = None
_chunks = None
_metadatas = None


def load_index():
    global _vectorizer, _tfidf_matrix, _chunks, _metadatas
    if _vectorizer is None:
        logger.info("Loading index...")
        with open(INDEX_DIR / "vectorizer.pkl", "rb") as f:
            _vectorizer = pickle.load(f)
        with open(INDEX_DIR / "tfidf_matrix.pkl", "rb") as f:
            _tfidf_matrix = pickle.load(f)
        with open(INDEX_DIR / "chunks.pkl", "rb") as f:
            _chunks = pickle.load(f)
        with open(INDEX_DIR / "metadatas.pkl", "rb") as f:
            _metadatas = pickle.load(f)
        logger.info(f"Loaded {len(_chunks)} chunks")
    return _vectorizer, _tfidf_matrix, _chunks, _metadatas


def search(query: str, top_k: int = 6):
    vectorizer, tfidf_matrix, chunks, metadatas = load_index()
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({
            "chunk": chunks[idx],
            "metadata": metadatas[idx],
            "score": float(scores[idx]),
        })
    return results


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[dict]] = None


class ChatResponse(BaseModel):
    reply: str
    sources: List[dict]


def build_prompt(query: str, context_chunks: List[str]) -> str:
    context = "\n\n---\n\n".join(context_chunks)
    return f"""你是一个个人知识助手，帮助用户整理和查询个人网站的内容。
请基于以下资料回答用户的问题。如果资料不足以回答，请诚实告知。
回答要简洁、有条理，使用中文。

参考资料：
{context}

用户问题：{query}

回答："""


@app.get("/api/health")
def health():
    try:
        _, _, chunks, _ = load_index()
        return {"status": "ok", "indexed_chunks": len(chunks)}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="DEEPSEEK_API_KEY not set")

    query = req.message.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Message is empty")

    try:
        results = search(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")

    if not results:
        return ChatResponse(reply="抱歉，我没有在网站内容中找到相关信息。", sources=[])

    chunks = [r["chunk"] for r in results]
    sources = [
        {
            "title": r["metadata"].get("title", "未知"),
            "path": r["metadata"].get("path", ""),
            "relevance": round(max(0, r["score"]), 3),
        }
        for r in results
    ]

    prompt = build_prompt(query, chunks)
    messages = [{"role": "system", "content": prompt}]
    if req.history:
        for msg in req.history[-10:]:
            if msg.get("role") in ("user", "assistant"):
                messages.append({"role": msg["role"], "content": msg["content"]})

    try:
        client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.3,
            max_tokens=2048,
        )
        reply = resp.choices[0].message.content
    except Exception as e:
        logger.error(f"DeepSeek API error: {e}")
        raise HTTPException(status_code=502, detail=f"AI service error: {e}")

    return ChatResponse(reply=reply, sources=sources)


def main():
    port = int(os.environ.get("CHAT_PORT", "5000"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")


if __name__ == "__main__":
    main()
