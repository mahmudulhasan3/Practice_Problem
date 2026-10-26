# generate_synthetic.py
import json
from google import genai

client = genai.Client()  # GEMINI_API_KEY .env থেকে

PROMPT = """You are creating test questions for a university assistant.
Given the passage below, write {n} questions a real student might ask
that can be answered ONLY using this passage.

Rules:
- Write like a real student: casual, sometimes Banglish, sometimes vague.
- Do NOT copy sentences from the passage into the question.
- Return JSON list: [{{"question": "...", "expected_answer": "..."}}]

Passage:
{chunk}
"""


def generate_for_chunk(chunk_text: str, doc: str, page: int, n: int = 2):
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT.format(n=n, chunk=chunk_text),
        config={"response_mime_type": "application/json"},
    )
    pairs = json.loads(resp.text) # type: ignore
    return [
        {
            "question": p["question"],
            "expected_answer": p["expected_answer"],
            "expected_sources": [{"doc": doc, "page": page}],
            "source_type": "synthetic",  # <- সবসময় mark করো
            "answerable": True,
        }
        for p in pairs
    ]
