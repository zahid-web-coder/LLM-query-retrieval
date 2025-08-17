import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Paths
INDEX_PATH = os.path.join("vector_index", "faiss_index.index")
CHUNKS_PATH = os.path.join("data", "all_chunks.jsonl")

# Load model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Load FAISS index
index = faiss.read_index(INDEX_PATH)

# Load chunks (corpus)
with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = [json.loads(line) for line in f]

def search(query, top_k=5):
    """
    Performs semantic search over document chunks using FAISS.

    Args:
        query (str): Natural language query
        top_k (int): Number of top results to return

    Returns:
        List of dicts with score, chunk_text, metadata
    """
    # Embed query
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx, score in zip(indices[0], distances[0]):
        if idx < len(chunks):
            chunk = chunks[idx]
            results.append({
                "score": float(score),
                "chunk_text": chunk.get("text", ""),
                "metadata": chunk.get("metadata", {})
            })

    return results

