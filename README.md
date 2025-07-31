# 📄 Agentic RAG Chatbot with MCP

A multi-format, agent-based Retrieval-Augmented Generation (RAG) chatbot that answers user questions using uploaded documents. Communication between agents follows the Model Context Protocol (MCP).

---

## 🚀 Features

- Upload and parse documents in:
  - PDF, PPTX, DOCX, CSV, TXT, MD
- Agentic architecture:
  - `IngestionAgent`, `RetrievalAgent`, `LLMResponseAgent`
- Vector store and semantic search using FAISS
- Embeddings via `SentenceTransformers (MiniLM)`
- LLM integration via OpenAI GPT-3.5 Turbo
- Streamlit-based UI for chatting and document upload
- Messages passed using MCP-like context objects

---

## 🧠 Architecture Overview

```plaintext
User Uploads Files + Query
        ↓
[UI (Streamlit)]
        ↓
[IngestionAgent] — extracts & embeds text
        ↓
[RetrievalAgent] — retrieves relevant chunks
        ↓
[LLMResponseAgent] — calls LLM & returns answer
        ↓
[UI] shows final answer + source context
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-openai-key-here
```

Or export it in your shell session:

```bash
export OPENAI_API_KEY="sk-..."
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Open the app in your browser (usually http://localhost:8501)
2. Upload one or more documents
3. Ask a question related to the uploaded content
4. View the generated answer and the source context

---

## 📦 Tech Stack

- Python
- Streamlit (UI)
- FAISS (Vector search)
- SentenceTransformers (Embeddings)
- OpenAI GPT-3.5 Turbo (LLM)
- PyPDF2, python-docx, python-pptx, csv (Document parsing)

---

## 📌 Folder Structure

```
.
├── app.py
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   └── llm_response_agent.py
├── utils/
│   ├── document_loader.py
│   └── embedding_utils.py
├── vector_store/
│   └── faiss_store.py
├── mcp.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧩 Future Improvements

- Add multi-turn conversation support
- Introduce `CoordinatorAgent` for orchestration
- Use persistent vector DB (e.g. Chroma)
- Add authentication and file storage

---

## 📄 License

MIT License
