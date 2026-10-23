# # REWRITE_PROMPT = """You rewrite a follow-up question into a standalone search query.

# # Rules:
# # - Use ONLY information from the chat history. Do NOT add new facts.
# # - Replace pronouns (it, this, that, এটা, ওটা) with what they refer to.
# # - Do NOT answer the question.
# # - Keep the same language as the user's question.
# # - If the question is already standalone, return it unchanged.
# # - Output ONLY the rewritten query. No quotes, no prefix, no explanation.

# # Chat history:
# # {history}

# # Follow-up question: {question}

# # Standalone query:"""
# # MAX_QUERY_WORDS = 40  # search query এর চেয়ে বেশি লম্বা হলে সন্দেহজনক
# # MAX_HISTORY_TURNS = 4  # শুধু শেষ কয়েকটা turn পাঠাব (cost + noise কমাতে)


# # def format_history(history: list[dict]) -> str:
# #     """শেষ N turn কে সাদামাটা text-এ রূপান্তর করে।"""
# #     recent = history[-MAX_HISTORY_TURNS * 2 :]
# #     return "\n".join(f"{m['role']}: {m['content']}" for m in recent)


# # def clean_output(text: str) -> str:
# #     """LLM যে অতিরিক্ত prefix/quote লাগায় সেগুলো ছাঁটে।"""
# #     text = text.strip().strip('"').strip("'").strip()
# #     for prefix in ("Rewritten query:", "Standalone query:", "Query:"):
# #         if text.lower().startswith(prefix.lower()):
# #             text = text[len(prefix) :].strip()
# #     return text


# # def is_valid_rewrite(original: str, rewritten: str) -> bool:
# #     """Rewritten query ব্যবহারযোগ্য কিনা যাচাই করে।"""
# #     if not rewritten:  # খালি
# #         return False
# #     if len(rewritten.split()) > MAX_QUERY_WORDS:  # অতিরিক্ত লম্বা = সম্ভবত উত্তর
# #         return False
# #     if "\n" in rewritten:  # multi-line = সম্ভবত paragraph
# #         return False
# #     return True


# # def rewrite_query(question: str, history: list[dict], llm) -> str:
# #     """নিরাপদ rewrite: কিছু ভুল হলে সবসময় original question ফেরত দেয়।"""
# #     try:
# #         prompt = REWRITE_PROMPT.format(
# #             history=format_history(history),
# #             question=question,
# #         )
# #         raw = llm.generate(prompt, temperature=0)  # deterministic output চাই
# #         rewritten = clean_output(raw)

# #         if is_valid_rewrite(question, rewritten):
# #             return rewritten
# #     except Exception:
# #         pass  # timeout, API error, যাই হোক

# #     return question  # FALLBACK: rewriter ব্যর্থ হলে original দিয়েই search


# from dataclasses import dataclass, field


# @dataclass
# class RAGResult:
#     """একটা request-এর পুরো ফলাফল। পরে logging/eval-এ কাজে লাগবে।"""

#     answer: str
#     original_question: str
#     search_query: str  # retriever-এ আসলে কোনটা গেল
#     was_rewritten: bool  # rewrite হয়েছিল কিনা
#     chunks: list = field(default_factory=list)


# def build_prompt(chunks: list, history: list[dict], question: str) -> str:
#     """LLM-এর জন্য final prompt। এখানে ORIGINAL question যায়।"""
#     context = "\n\n".join(f"[{i+1}] {c['text']}" for i, c in enumerate(chunks))
#     return (
#         "Answer using ONLY the context below. Cite sources like [1].\n"
#         "If the context doesn't contain the answer, say you don't know.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Chat history:\n{format_history(history)}\n\n"
#         f"Question: {question}\n"
#         "Answer:"
#     )


# def answer_question(question: str, history: list[dict], llm) -> RAGResult:
#     # Step 1: rewrite দরকার কিনা, দরকার হলে rewrite
#     if needs_rewrite(question, history):
#         search_query = rewrite_query(question, history, llm)
#     else:
#         search_query = question
#     was_rewritten = search_query != question

#     # Step 2: retrieval আর reranking দুটোই rewritten query দিয়ে
#     candidates = hybrid_search(search_query, top_k=10)
#     chunks = rerank(search_query, candidates, top_k=3)

#     # Step 3: LLM-কে ORIGINAL question দিয়ে answer generate করাও
#     prompt = build_prompt(chunks, history, question)
#     answer = llm.generate(prompt, temperature=0.2)

#     return RAGResult(
#         answer=answer,
#         original_question=question,
#         search_query=search_query,
#         was_rewritten=was_rewritten,
#         chunks=chunks,
#     )


# # প্রতিটা case: কোন source/chunk retrieve হওয়া উচিত সেটা আমরা আগে থেকে জানি
# TEST_CASES = [
#     {
#         "id": "pronoun_followup",
#         "history": [
#             {"role": "user", "content": "What is multi-head attention?"},
#             {
#                 "role": "assistant",
#                 "content": "It runs several attention operations in parallel...",
#             },
#         ],
#         "question": "কেন এটা দরকার?",
#         "expected_source": "attention_is_all_you_need.pdf",  # তোমার আসল doc নাম বসাও
#     },
#     {
#         "id": "standalone",  # rewrite দরকার নেই, control case
#         "history": [],
#         "question": "How does BM25 rank documents?",
#         "expected_source": "bm25_paper.pdf",
#     },
#     {
#         "id": "mixed_language",
#         "history": [
#             {"role": "user", "content": "Reranker কী?"},
#             {"role": "assistant", "content": "Reranker হলো ..."},
#         ],
#         "question": "এটার latency কত?",
#         "expected_source": "reranking_paper.pdf",
#     },
#     # আরও ৭-১০টা যোগ করো
# ]


# def hit_at_k(chunks: list, expected_source: str) -> bool:
#     """Top-k chunk-এর মধ্যে expected source আছে কিনা।"""
#     return any(c["source"] == expected_source for c in chunks)


# def evaluate(test_cases: list, llm, use_rewrite: bool, top_k: int = 3) -> dict:
#     hits = 0
#     failures = []

#     for case in test_cases:
#         q, history = case["question"], case["history"]

#         # শুধু rewrite ON/OFF বদলাচ্ছে, বাকি সব হুবহু এক
#         if use_rewrite and needs_rewrite(q, history):
#             search_query = rewrite_query(q, history, llm)
#         else:
#             search_query = q

#         candidates = hybrid_search(search_query, top_k=10)
#         chunks = rerank(search_query, candidates, top_k=top_k)

#         if hit_at_k(chunks, case["expected_source"]):
#             hits += 1
#         else:
#             failures.append({"id": case["id"], "search_query": search_query})

#     return {"hit_rate": hits / len(test_cases), "failures": failures}


# off = evaluate(TEST_CASES, llm, use_rewrite=False)
# on = evaluate(TEST_CASES, llm, use_rewrite=True)

# print(f"Rewrite OFF: {off['hit_rate']:.0%}")
# print(f"Rewrite ON : {on['hit_rate']:.0%}")
# print("Still failing:", on["failures"])


# def test_rewriter_does_not_answer():
#     history = [
#         {"role": "user", "content": "What is BM25?"},
#         {"role": "assistant", "content": "A ranking function..."},
#     ]
#     out = rewrite_query("এটা কীভাবে কাজ করে?", history, llm)
#     assert "?" in out or len(out.split()) < 25  # উত্তর না, query চাই
#     assert "BM25" in out  # pronoun সঠিকভাবে replace হয়েছে


# def test_rewriter_falls_back_on_failure():
#     broken_llm = BrokenLLM()  # যে সবসময় exception ছোড়ে
#     assert rewrite_query("এটা কী?", [], broken_llm) == "এটা কী?"


"""
Day 130: Query Rewriting (final polish pass)

Run:  python day130_query_rewriting.py
(FakeLLM + tiny in-memory corpus ব্যবহার করা হয়েছে, তাই API key ছাড়াই চলবে।)

নিজের project-এ বসানোর সময়:
  1. FakeLLM বাদ দিয়ে তোমার আসল llm object দাও (যার .generate(prompt, temperature) আছে)
  2. hybrid_search / rerank stub বাদ দিয়ে Day 129-এর আসল function import করো
"""

import json
import logging
import time
import uuid
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
logger = logging.getLogger("rag.rewrite")

# ───────────────────────── Config ─────────────────────────
MAX_QUERY_WORDS = 40  # এর চেয়ে লম্বা rewrite = সম্ভবত উত্তর দিয়ে ফেলেছে
MAX_HISTORY_TURNS = 4  # শুধু শেষ ৪ turn (cost + noise কমাতে)
SHORT_QUESTION_WORDS = 6

# Pronoun/reference শব্দ: এগুলো থাকলে question আগের কথার উপর নির্ভর করছে
FOLLOWUP_HINTS = {
    "it",
    "its",
    "this",
    "that",
    "they",
    "them",
    "these",
    "those",
    "এটা",
    "ওটা",
    "সেটা",
    "এটার",
    "ওটার",
    "এগুলো",
}

REWRITE_PROMPT = """You rewrite a follow-up question into a standalone search query.

Rules:
- Use ONLY information from the chat history. Do NOT add new facts.
- Replace pronouns (it, this, that, এটা, ওটা) with what they refer to.
- Do NOT answer the question.
- Keep the same language as the user's question.
- Keep English technical terms as they are.
- If the question is already standalone, return it unchanged.
- Output ONLY the rewritten query. No quotes, no prefix, no explanation.

Chat history:
{history}

Follow-up question: {question}

Standalone query:"""


# ───────────────────────── Step 1: Gate ─────────────────────────
def needs_rewrite(question: str, history: list[dict]) -> bool:
    """Rewrite দরকার কিনা। সন্দেহ হলে True (False Negative বেশি ক্ষতিকর)।"""
    if not history:  # প্রথম message: rewrite করার কিছু নেই
        return False

    words = question.lower().split()
    if len(words) <= SHORT_QUESTION_WORDS:  # ছোট question = context-dependent
        return True

    cleaned = {w.strip("?.,!।") for w in words}
    return bool(cleaned & FOLLOWUP_HINTS)  # pronoun আছে কিনা


# ───────────────────────── Step 2: Rewriter + validation ─────────────────────────
def format_history(history: list[dict]) -> str:
    recent = history[-MAX_HISTORY_TURNS * 2 :]
    return "\n".join(f"{m['role']}: {m['content']}" for m in recent)


def clean_output(text: str) -> str:
    """LLM-এর বাড়তি quote/prefix ছাঁটে।"""
    text = text.strip()
    # আগে prefix সরাও, তারপর quote (উল্টো করলে ভিতরের quote থেকে যায়)
    for prefix in ("Rewritten query:", "Standalone query:", "Query:"):
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix) :].strip()
    return text.strip('"').strip("'").strip()


def is_valid_rewrite(rewritten: str) -> bool:
    if not rewritten:  # খালি
        return False
    if len(rewritten.split()) > MAX_QUERY_WORDS:  # অতিরিক্ত লম্বা
        return False
    if "\n" in rewritten:  # multi-line = paragraph
        return False
    return True


def rewrite_with_status(question: str, history: list[dict], llm) -> tuple[str, str]:
    """
    (search_query, status) ফেরত দেয়।
    status: skipped | rewritten | unchanged | fallback
    """
    if not needs_rewrite(question, history):
        return question, "skipped"

    try:
        prompt = REWRITE_PROMPT.format(
            history=format_history(history), question=question
        )
        raw = llm.generate(prompt, temperature=0)  # deterministic
        rewritten = clean_output(raw)

        if is_valid_rewrite(rewritten):
            return rewritten, ("unchanged" if rewritten == question else "rewritten")
    except Exception:
        logger.exception("rewriter failed")

    return question, "fallback"  # graceful degradation


# ───────────────────────── Step 3: Full chain ─────────────────────────
@dataclass
class RAGResult:
    answer: str
    original_question: str
    search_query: str
    rewrite_status: str
    chunks: list = field(default_factory=list)


def build_prompt(chunks: list, history: list[dict], question: str) -> str:
    """LLM-এর final prompt। এখানে ORIGINAL question যায়, rewritten না।"""
    context = "\n\n".join(f"[{i + 1}] {c['text']}" for i, c in enumerate(chunks))
    return (
        "Answer using ONLY the context below. Cite sources like [1].\n"
        "If the context doesn't contain the answer, say you don't know.\n\n"
        f"Context:\n{context}\n\n"
        f"Chat history:\n{format_history(history)}\n\n"
        f"Question: {question}\n"
        "Answer:"
    )


def answer_question(question: str, history: list[dict], llm) -> RAGResult:
    request_id = uuid.uuid4().hex[:8]

    # rewrite step আলাদা করে মাপছি
    t0 = time.perf_counter()
    search_query, status = rewrite_with_status(question, history, llm)
    rewrite_ms = (time.perf_counter() - t0) * 1000

    # retrieval + rerank: দুটোই REWRITTEN query দিয়ে
    candidates = hybrid_search(search_query, top_k=10)
    chunks = rerank(search_query, candidates, top_k=3)

    logger.info(
        "rewrite_step %s",
        json.dumps(
            {
                "request_id": request_id,
                "original_question": question,
                "search_query": search_query,
                "rewrite_status": status,
                "rewrite_latency_ms": round(rewrite_ms, 1),
                "top_sources": [c["source"] for c in chunks],
            },
            ensure_ascii=False,
        ),
    )

    # LLM-কে ORIGINAL question
    answer = llm.generate(build_prompt(chunks, history, question), temperature=0.2)
    return RAGResult(answer, question, search_query, status, chunks)


# ───────────────────────── Step 4: Evaluation (rewrite ON vs OFF) ─────────────────────────
def hit_at_k(chunks: list, expected_source: str) -> bool:
    return any(c["source"] == expected_source for c in chunks)


def evaluate(test_cases: list[dict], llm, use_rewrite: bool, top_k: int = 3) -> dict:
    hits, failures = 0, []
    for case in test_cases:
        q, history = case["question"], case["history"]
        if use_rewrite:
            search_query, _ = rewrite_with_status(q, history, llm)
        else:
            search_query = q

        chunks = rerank(
            search_query, hybrid_search(search_query, top_k=10), top_k=top_k
        )
        if hit_at_k(chunks, case["expected_source"]):
            hits += 1
        else:
            failures.append({"id": case["id"], "search_query": search_query})
    return {"hit_rate": hits / len(test_cases), "failures": failures}


# ═════════════════════════ DEMO SUPPORT (এই অংশ তোমার আসল code দিয়ে replace করো) ═════════════════════════
CORPUS = [
    {
        "source": "attention.pdf",
        "text": "multi-head attention lets the model attend to different representation subspaces in parallel",
    },
    {
        "source": "bm25.pdf",
        "text": "BM25 is a ranking function based on term frequency and document length",
    },
    {
        "source": "reranking.pdf",
        "text": "a reranker scores query document pairs and adds latency compared to vector search only",
    },
]


def hybrid_search(query: str, top_k: int = 10) -> list[dict]:
    """STUB: word-overlap দিয়ে scoring। Day 125-এর আসল hybrid retrieval বসাও।"""
    q = set(query.lower().replace("?", "").split())
    scored = [(len(q & set(d["text"].lower().split())), d) for d in CORPUS]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:top_k]]


def rerank(query: str, candidates: list[dict], top_k: int = 3) -> list[dict]:
    """STUB: আসল reranker (Day 126) বসাও।"""
    return candidates[:top_k]


class FakeLLM:
    """API ছাড়া demo চালানোর জন্য নকল LLM।"""

    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        if prompt.startswith("You rewrite"):
            if "multi-head" in prompt:
                return "multi-head attention কেন দরকার?"
            if "BM25" in prompt:
                return "BM25 downside কী?"
            return "reranker latency কত?"
        return "(fake answer) [1]"


class BrokenLLM:
    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        raise RuntimeError("API down")


# ═════════════════════════ Tests ═════════════════════════
def run_tests() -> None:
    h = [
        {"role": "user", "content": "What is BM25?"},
        {"role": "assistant", "content": "A ranking function"},
    ]

    # Gate
    assert needs_rewrite("hello there", []) is False  # history নেই
    assert needs_rewrite("আর এটার downside কী?", h) is True  # pronoun + ছোট
    assert (
        needs_rewrite(
            "Explain the difference between BM25 and dense retrieval in detail", h
        )
        is False
    )

    # Output cleaning + validation
    assert clean_output('Rewritten query: "BM25 downside"') == "BM25 downside"
    assert is_valid_rewrite("") is False
    assert is_valid_rewrite("word " * 50) is False

    # Fallback: rewriter ভাঙলে original ফেরত আসবে, crash করবে না
    q, status = rewrite_with_status("এটা কী?", h, BrokenLLM())
    assert (q, status) == ("এটা কী?", "fallback")

    # Original question LLM prompt-এ যায়
    r = answer_question(
        "কেন এটা দরকার?",
        [
            {"role": "user", "content": "What is multi-head attention?"},
            {"role": "assistant", "content": "parallel attention"},
        ],
        FakeLLM(),
    )
    assert r.search_query != r.original_question and r.rewrite_status == "rewritten"
    print("✅ all tests passed")


if __name__ == "__main__":
    run_tests()

    TEST_CASES = [
        {
            "id": "pronoun_followup",
            "history": [
                {"role": "user", "content": "What is multi-head attention?"},
                {"role": "assistant", "content": "parallel attention"},
            ],
            "question": "কেন এটা দরকার?",
            "expected_source": "attention.pdf",
        },
        {
            "id": "control_standalone",
            "history": [],
            "question": "How does BM25 rank documents?",
            "expected_source": "bm25.pdf",
        },
    ]
    llm = FakeLLM()
    print("Rewrite OFF:", evaluate(TEST_CASES, llm, use_rewrite=False))
    print("Rewrite ON :", evaluate(TEST_CASES, llm, use_rewrite=True))
