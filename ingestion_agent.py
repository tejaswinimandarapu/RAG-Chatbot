# agents/ingestion_agent.py
from utils.document_loader import extract_text
from utils.embedding_utils import embed_text
from vector_store.faiss_store import VectorStore
from mcp import build_message

vector_store = VectorStore()

def process_files(file_paths, trace_id):
    all_chunks = []
    for path in file_paths:
        raw = extract_text(path)
        if not raw or not raw.strip():
            print(f"WARNING: No content extracted from {path}, skipping.")
            continue
        
        # Chunk using fixed-size (you could also use listener or semantic splitters)
        chunks = [raw[i:i+500] for i in range(0, len(raw), 500)]
        if not chunks:
            print(f"WARNING: No chunks created from {path}, skipping.")
            continue

        embeds = embed_text(chunks)

        # Validation: embeddings count should match chunks count
        if len(embeds) != len(chunks):
            print(f"ERROR: embed count {len(embeds)} != chunk count {len(chunks)} for {path}")
            continue

        vector_store.add(embeds, chunks)
        all_chunks.extend(chunks)

    return build_message(
        "IngestionAgent",
        "RetrievalAgent",
        "INGESTION_COMPLETE",
        trace_id,
        {"chunks": all_chunks}
    )

