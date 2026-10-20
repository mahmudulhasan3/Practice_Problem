# from dataclasses import dataclass


# @dataclass
# class Chunk:
#     chunk_id: str
#     text: str
#     source: str  # file name
#     page: int
#     score: float  # retrieval score


# def make_preview(chunk: Chunk, max_chars: int = 200) -> dict:
    
#     text = " ".join(chunk.text.split())

#     if len(text) > max_chars:
#         text = text[:max_chars].rsplit(" ", 1)[0] + "..."

#     return {
#         "chunk_id": chunk.chunk_id,
#         "source": chunk.source,
#         "page": chunk.page,
#         "score": round(chunk.score, 3),
#         "snippet": text,
#     }

# EVIDENCE_PROMPT = """
# Answer the question using ONLY the context chunks below.
# For every claim, return evidence as JSON.

# Rules:
# - "quote" must be copied EXACTLY from the chunk. Do not paraphrase.
# - If no chunk supports a claim, do not make that claim.

# Return JSON only:
# {{"claims": [{{"claim": "...", "chunk_id": "...", "quote": "..."}}]}}

# Context:
# {context}

# Question: {question}
# """


# def build_context(chunks: list[Chunk]) -> str:
#     return "\n\n".join(f"[{c.chunk_id}]\n{c.text}" for c in chunks)


# from difflib import SequenceMatcher


# def normalize(s: str) -> str:
    
#     return " ".join(s.lower().split())


# def quote_in_chunk(quote: str, chunk_text: str, threshold: float = 0.9):
#     q, c = normalize(quote), normalize(chunk_text)

#     # Case 1: exact substring
#     if q in c:
#         return True, 1.0

#     # Case 2: fuzzy. PDF extraction-এ ছোট গরমিল থাকে (hyphen, ligature)
#     match = SequenceMatcher(None, q, c).find_longest_match(0, len(q), 0, len(c))
#     ratio = match.size / max(len(q), 1)
#     return ratio >= threshold, ratio


# def verify_citation(item: dict, retrieved: dict[str, Chunk]) -> dict:
#     chunk = retrieved.get(item["chunk_id"])

#     # Level 1: fake source?
#     if chunk is None:
#         return {**item, "status": "fake_source"}

#     # Level 2: quote আছে?
#     ok, ratio = quote_in_chunk(item["quote"], chunk.text)
#     if not ok:
#         return {**item, "status": "quote_not_found", "match": round(ratio, 2)}

#     return {**item, "status": "verified", "match": round(ratio, 2)}


# def answer_with_verified_evidence(question, chunks, llm_call):
#     retrieved = {c.chunk_id: c for c in chunks}
#     raw = llm_call(
#         EVIDENCE_PROMPT.format(context=build_context(chunks), question=question)
#     )
#     claims = parse_json(raw)["claims"]  # Day 43-এর structured output validation

#     results = [verify_citation(item, retrieved) for item in claims]

#     return {
#         "verified": [r for r in results if r["status"] == "verified"],
#         "rejected": [r for r in results if r["status"] != "verified"],
#         "previews": [make_preview(c) for c in chunks],
#     }
