# agents/retrieval_agent.py
from utils.embedding_utils import model
from mcp import build_message
from vector_store.faiss_store import VectorStore
import numpy as np

vector_store = VectorStore()  # ✅ Create an instance

def retrieve_context(query, trace_id):
    query_embedding = model.encode([query])[0]
    print("DEBUG: type(query_embedding):", type(query_embedding))
    if isinstance(query_embedding, list):
        print("DEBUG: first few elements:", query_embedding[:5])
    
    arr = np.asarray(query_embedding, dtype="float32")
    print("DEBUG: np array shape:", arr.shape, "ndim:", arr.ndim)
    assert arr.ndim == 1, f"Expected a single (1D) query embedding vector, got ndim={arr.ndim}"

    # ✅ Use instance method safely
    top_chunks = vector_store.search(query_embedding)

    # ✅ Fallback if no context retrieved
    if not top_chunks:
        top_chunks = ["⚠️ No relevant context found."]

    return build_message("RetrievalAgent", "LLMResponseAgent", "RETRIEVAL_RESULT", trace_id, {
        "retrieved_context": top_chunks,
        "query": query
    })
