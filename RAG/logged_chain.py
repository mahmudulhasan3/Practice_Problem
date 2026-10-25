import os
import time
import uuid

import psycopg2
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from full_retrieve import retrieve

load_dotenv()

# ---------- Config ----------
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.1-flash-lite")
PROMPT_VERSION = "v1"
CANDIDATES = 10
FINAL_K = 3

llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0)

# ---------- Prompts ----------
rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Rewrite the user's question as a standalone search query. "
            "Return only the query, nothing else.",
        ),
        ("human", "{question}"),
    ]
)

answer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer using only the given context. "
            "If the answer is not in the context, say you don't have the information.",
        ),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ]
)


# ---------- Helpers ----------
def get_text(response):
    """AIMessage থেকে text বের করে (content string বা list-of-blocks দুটোই সামলায়)।"""
    content = response.content
    if isinstance(content, str):
        return content
    return "".join(
        block.get("text", "") for block in content if isinstance(block, dict)
    )


def get_usage(response):
    """AIMessage থেকে input/output token বের করে।"""
    usage = response.usage_metadata or {}
    return {
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
    }


def format_context(docs):
    """Document গুলোকে source label সহ একটা text বানায়।"""
    parts = []
    for d in docs:
        source = d.metadata.get("filename", d.metadata.get("source", "unknown"))
        page = d.metadata.get("page", "?")
        parts.append(f"[{source} | page {page}]\n{d.page_content}")
    return "\n\n".join(parts)


# ---------- LLM stages  ----------
def rewrite_query(question):
    response = (rewrite_prompt | llm).invoke({"question": question})
    return get_text(response).strip(), get_usage(response)


def generate_answer(question, docs):
    context = format_context(docs)
    response = (answer_prompt | llm).invoke({"context": context, "question": question})
    return get_text(response), get_usage(response)


# ---------- DB ----------
def save_log(log: dict):
    """একটা request এর পুরো log একটা row হিসেবে save করে।"""
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO rag_request_logs (
                    request_id, user_id, session_id,
                    model_name, prompt_version, candidates, final_k,
                    rewrite_ms, retrieve_ms, generate_ms, total_ms,
                    rewrite_input_tokens, rewrite_output_tokens,
                    answer_input_tokens, answer_output_tokens,
                    status, error_message
                ) VALUES (
                    %(request_id)s, %(user_id)s, %(session_id)s,
                    %(model_name)s, %(prompt_version)s, %(candidates)s, %(final_k)s,
                    %(rewrite_ms)s, %(retrieve_ms)s, %(generate_ms)s, %(total_ms)s,
                    %(rewrite_input_tokens)s, %(rewrite_output_tokens)s,
                    %(answer_input_tokens)s, %(answer_output_tokens)s,
                    %(status)s, %(error_message)s
                )
                """,
                log,
            )
    finally:
        conn.close()


# ---------- Main pipeline with logging ----------
def answer_with_logging(question, user_id="u1", session_id="s1"):
    log = {
        "request_id": str(uuid.uuid4()),
        "user_id": user_id,
        "session_id": session_id,
        "model_name": MODEL_NAME,
        "prompt_version": PROMPT_VERSION,
        "candidates": CANDIDATES,
        "final_k": FINAL_K,
        "rewrite_ms": None,
        "retrieve_ms": None,
        "generate_ms": None,
        "total_ms": None,
        "rewrite_input_tokens": None,
        "rewrite_output_tokens": None,
        "answer_input_tokens": None,
        "answer_output_tokens": None,
        "status": "success",
        "error_message": None,
    }

    total_start = time.perf_counter()

    try:
        # Stage 1: rewrite
        start = time.perf_counter()
        standalone_q, usage = rewrite_query(question)
        log["rewrite_ms"] = (time.perf_counter() - start) * 1000
        log["rewrite_input_tokens"] = usage["input_tokens"]
        log["rewrite_output_tokens"] = usage["output_tokens"]

        # Stage 2: retrieve (hybrid + rerank)
        start = time.perf_counter()
        docs = retrieve(standalone_q)
        log["retrieve_ms"] = (time.perf_counter() - start) * 1000

        # Stage 3: generate
        start = time.perf_counter()
        answer, usage = generate_answer(question, docs)
        log["generate_ms"] = (time.perf_counter() - start) * 1000
        log["answer_input_tokens"] = usage["input_tokens"]
        log["answer_output_tokens"] = usage["output_tokens"]

        return answer

    except Exception as e:
        log["status"] = "error"
        log["error_message"] = str(e)
        raise

    finally:
        log["total_ms"] = (time.perf_counter() - total_start) * 1000
        save_log(log)


# ---------- Runner ----------
if __name__ == "__main__":
    questions = [
        "What is self-attention?",
        "What is multi-head attention?",
        "Why does the Transformer use positional encoding?",
        "What is the Transformer architecture?",
        "What is scaled dot-product attention?",
        "How does the encoder differ from the decoder?",
        "What is the lost in the middle problem?",
        "What is retrieval-augmented generation?",
        "How does BERT use bidirectional training?",
        "What is masked language modeling?",
        "What is the role of layer normalization?",
        "What is beam search?",
    ]

    for q in questions:
        try:
            answer = answer_with_logging(q)
            print(f"Q: {q}\nA: {answer[:120]}...\n")
        except Exception as e:
            print(f"FAILED: {q} -> {e}\n")

        time.sleep(10)
