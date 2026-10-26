# eval_retrieval.py
def evaluate_retrieval(items, retrieve_fn, k: int = 5):
    """
    retrieve_fn(question) -> list of {"doc": ..., "page": ...}
    Hit@k : expected source top-k এর মধ্যে আছে কিনা
    MRR   : expected source কত উপরে এসেছে
    """
    hits, rr_sum, n = 0, 0.0, 0

    for item in items:
        if not item.answerable:  # unanswerable গুলো আলাদা test হবে
            continue
        n += 1
        results = retrieve_fn(item.question)[:k]
        expected = {(s.doc, s.page) for s in item.expected_sources}

        rank = next(
            (i + 1 for i, r in enumerate(results) if (r["doc"], r["page"]) in expected),
            None,
        )
        if rank:
            hits += 1
            rr_sum += 1 / rank

    return {"hit@k": hits / n, "mrr": rr_sum / n, "n": n}
