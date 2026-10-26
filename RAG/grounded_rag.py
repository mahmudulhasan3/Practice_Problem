# grounded_rag.py
import json
from google import genai

client = genai.Client()

IDK = "দুঃখিত, প্রদত্ত document-এ এই প্রশ্নের উত্তর পাওয়া যায়নি।"
SCORE_THRESHOLD = (
    0.55  # embedding model অনুযায়ী বদলায়, golden dataset দিয়ে tune করবে
)

PROMPT = """You are a university assistant. Answer ONLY using the context below.

Rules:
1. If the context does not contain the answer, set "answerable" to false.
2. Never use outside knowledge.
3. Every answer must cite the chunk ids you used.
4. Answer in the same language as the question.

Return JSON only:
{{"answerable": true/false, "answer": "...", "citations": ["chunk_id", ...]}}

Context:
{context}

Question: {question}
"""


def answer(question: str, retrieve_fn) -> dict:
    # retrieve_fn(question) -> [{"id","text","doc","page","score"}, ...] (score বেশি = ভালো)
    chunks = retrieve_fn(question)

    # স্তর 1: Retrieval gate
    if not chunks or chunks[0]["score"] < SCORE_THRESHOLD:
        return {
            "answer": IDK,
            "citations": [],
            "abstained": True,
            "reason": "low_retrieval_score",
        }

    context = "\n\n".join(f"[{c['id']}] {c['text']}" for c in chunks)

    # স্তর 2: Grounded prompt, temperature=0 যাতে বানানোর সুযোগ কমে
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT.format(context=context, question=question),
        config={"response_mime_type": "application/json", "temperature": 0},
    )
    try:
        data = json.loads(resp.text) #type: ignore
    except json.JSONDecodeError:
        return {"answer": IDK, "citations": [], "abstained": True, "reason": "bad_json"}

    # স্তর 3: Citation validation
    valid_ids = {c["id"] for c in chunks}
    cited = [
        cid for cid in data.get("citations", []) if cid in valid_ids
    ]  # বানানো id ফেলে দাও

    if not data.get("answerable") or not cited:
        return {
            "answer": IDK,
            "citations": [],
            "abstained": True,
            "reason": "no_grounded_answer",
        }

    return {"answer": data["answer"], "citations": cited, "abstained": False}


JUDGE_PROMPT = """Context:
{context}

Answer:
{answer}

Split the answer into individual claims. For each claim say whether it is
SUPPORTED or UNSUPPORTED by the context. Return JSON:
{{"claims": [{{"claim": "...", "verdict": "SUPPORTED|UNSUPPORTED"}}]}}
"""
# কোনো claim UNSUPPORTED হলে → উত্তর বাতিল করো বা সেই অংশ বাদ দাও


def eval_hallucination(items, answer_fn, retrieve_fn):
    halluc, false_abstain, n_unans, n_ans = 0, 0, 0, 0
    for it in items:
        out = answer_fn(it.question, retrieve_fn)
        if not it.answerable:
            n_unans += 1
            if not out["abstained"]:  # জানি না বলা উচিত ছিল, বলেনি
                halluc += 1
        else:
            n_ans += 1
            if out["abstained"]:  # উত্তর দেওয়া উচিত ছিল, দেয়নি
                false_abstain += 1
    return {
        "hallucination_rate": halluc / max(n_unans, 1),
        "false_abstain_rate": false_abstain / max(n_ans, 1),
    }
