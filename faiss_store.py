import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)  # 384 = dim for MiniLM
        self.text_chunks = []

    def add(self, embeddings, chunks):
        arr = np.asarray(embeddings, dtype="float32")
        print("DEBUG: type(embeddings):", type(embeddings))
        if isinstance(embeddings, list) and embeddings:
            print("DEBUG: type of first item:", type(embeddings[0]))

        print("DEBUG: numpy embeddings shape:", arr.shape, "ndim:", arr.ndim)
        assert arr.ndim == 2, f"Embeddings must be 2D array (num_vectors × dimension), got ndim={arr.ndim}"

        if chunks is not None:
            assert arr.shape[0] == len(chunks), (
                f"Mismatch: {arr.shape[0]} embeddings vs {len(chunks)} chunks"
            )

        self.text_chunks.extend(chunks)
        self.index.add(arr)

    def search(self, query_embed, k=5):
        query_arr = np.array([query_embed], dtype="float32")
        D, I = self.index.search(query_arr, k)

        results = []
        for i in I[0]:
            if 0 <= i < len(self.text_chunks):
                results.append(self.text_chunks[i])

        return results