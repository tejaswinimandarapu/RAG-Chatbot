# utils/embedding_utils.py
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(chunks):
    arr = model.encode(chunks, convert_to_tensor=False)
    arr = np.atleast_2d(arr)  # ensure shape (1, dim) even if only one chunk
    return arr.astype('float32').tolist()
