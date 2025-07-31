import openai
import os
from mcp import build_message
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY", "your-fallback-api-key")

def generate_answer(payload, trace_id):
    context = "\n".join(payload["retrieved_context"])
    query = payload["query"]

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        answer = response.choices[0].message.content.strip()

        return build_message("LLMResponseAgent", "UI", "FINAL_ANSWER", trace_id, {
            "answer": answer,
            "sources": payload["retrieved_context"]
        })

    except Exception as e:
        return build_message("LLMResponseAgent", "UI", "FINAL_ANSWER", trace_id, {
            "answer": f"⚠️ LLM generation failed: {str(e)}",
            "sources": payload["retrieved_context"]
        })