import json
from collections import defaultdict


# ---------- ১. Dataset load ----------
def load_jsonl(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # খালি লাইন বাদ
                records.append(json.loads(line))
    return records


# ---------- ২. Citation-কে set-এর উপাদান বানানো ----------
def to_key_set(citations):
    # [{"filename": "a.pdf", "page": 4}] -> {("a.pdf", 4)}
    return {(c["filename"], c["page"]) for c in citations}


# ---------- ৩. Precision / Recall ----------
def citation_scores(expected, actual):
    exp = to_key_set(expected)
    act = to_key_set(actual)

    # দুটোই খালি: উত্তর নেই, system ঠিকমতো citation দেয়নি
    if not exp and not act:
        return {"precision": 1.0, "recall": 1.0}

    # একপাশ খালি, অন্যপাশ না: 0 দিয়ে ভাগ এড়াতে
    if not exp or not act:
        return {"precision": 0.0, "recall": 0.0}

    tp = len(exp & act)
    return {
        "precision": tp / len(act),  # হর = actual
        "recall": tp / len(exp),  # হর = expected
    }


# ---------- ৪. নকল RAG system (practice-এর জন্য) ----------
def _c(filename, page):
    return {"filename": filename, "page": page}


FAKE_RESULTS = {
    "What is the Transformer architecture based on?": [_c("1706.pdf", 1)],  # ঠিক
    "How many layers does the encoder have?": [_c("1706.pdf", 3)],  # ঠিক
    "What optimizer was used for training?": [_c("1706.pdf", 9)],  # ভুল page
    "Why is multi-head attention used?": [_c("1706.pdf", 4)],  # একটা বাদ
    "How does positional encoding work?": [
        _c("1706.pdf", 5),
        _c("1706.pdf", 6),
        _c("1706.pdf", 9),
    ],  # একটা বেশি
    "Compare Transformer and BERT pretraining objectives.": [
        _c("1706.pdf", 6)
    ],  # bert.pdf বাদ
    "Who won the 2022 FIFA World Cup?": [],  # ঠিক, কিছু cite করেনি
    "What is the capital of Bangladesh?": [_c("1706.pdf", 4)],  # বানানো citation
}


def fake_rag_answer(question):
    return {"answer": "...", "citations": FAKE_RESULTS[question]}


# ---------- ৫. পুরো dataset-এ চালানো ----------
def evaluate(records, rag_answer):
    rows = []
    for r in records:
        result = rag_answer(r["question"])
        scores = citation_scores(r["expected_citations"], result["citations"])
        rows.append(
            {
                "id": r["id"],
                "category": r["category"],
                "precision": scores["precision"],
                "recall": scores["recall"],
            }
        )
    return rows


# ---------- ৬. Score table ----------
def summarize(rows):
    # প্রতিটা প্রশ্ন আলাদা করে
    print("--- Per question ---")
    for row in rows:
        print(
            f'{row["id"]}  {row["category"]:14} '
            f'P={row["precision"]:.2f}  R={row["recall"]:.2f}'
        )

    # Category অনুযায়ী গড়
    by_cat = defaultdict(list)
    for row in rows:
        by_cat[row["category"]].append(row)

    print("\n--- Per category ---")
    for cat, items in by_cat.items():
        avg_p = sum(i["precision"] for i in items) / len(items)
        avg_r = sum(i["recall"] for i in items) / len(items)
        print(f"{cat:14} n={len(items):2}  P={avg_p:.2f}  R={avg_r:.2f}")

    # মোট গড়
    total_p = sum(r["precision"] for r in rows) / len(rows)
    total_r = sum(r["recall"] for r in rows) / len(rows)
    print(f"\nOVERALL        n={len(rows):2}  P={total_p:.2f}  R={total_r:.2f}")


if __name__ == "__main__":
    records = load_jsonl("RAG/golden_dev.jsonl")
    rows = evaluate(records, fake_rag_answer)
    summarize(rows)
