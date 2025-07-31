# app.py
import streamlit as st
import uuid
import tempfile
from agents.ingestion_agent import process_files
from agents.retrieval_agent import retrieve_context
from agents.llm_response_agent import generate_answer

st.title("📄 Agentic RAG Chatbot with MCP")
uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)
query = st.text_input("Ask a question")

if uploaded_files and query:
    with st.spinner("Processing..."):
        temp_paths = []
        for file in uploaded_files:
            temp_path = tempfile.NamedTemporaryFile(delete=False).name
            with open(temp_path, "wb") as f:
                f.write(file.read())
            temp_paths.append(temp_path)

        trace_id = str(uuid.uuid4())
        msg1 = process_files(temp_paths, trace_id)
        msg2 = retrieve_context(query, trace_id)
        msg3 = generate_answer(msg2["payload"], trace_id)

        st.subheader("Answer:")
        st.write(msg3["payload"]["answer"])

        with st.expander("📄 Source Context"):
            for chunk in msg3["payload"]["sources"]:
                st.markdown(f"> {chunk}")
