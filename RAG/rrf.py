# rrf.py : দুই (বা বেশি) retriever-এর result merge করার function


def make_key(doc):
    # একই file + একই page + একই text = একই chunk
    return f"{doc.metadata['source']}|{doc.metadata['page']}|{doc.page_content}"


def rrf(result_lists, k=60):
    scores = {}  # key -> মোট RRF score
    docs = {}  # key -> আসল Document

    for results in result_lists:  # একটা একটা retriever
        for rank, doc in enumerate(results, start=1):  # ওই list-এ rank (1 থেকে)
            key = make_key(doc)
            docs[key] = doc
            scores[key] = scores.get(key, 0) + 1 / (k + rank)

    ranked_keys = sorted(scores, key=scores.get, reverse=True)  # type: ignore
    return [(docs[key], scores[key]) for key in ranked_keys]


if __name__ == "__main__":
    # fake data দিয়ে test (সরাসরি run করলেই শুধু চলবে)
    from langchain_core.documents import Document

    def fake(name):
        return Document(page_content=name, metadata={"source": "x.pdf", "page": 0})

    A, B, C, D = fake("A"), fake("B"), fake("C"), fake("D")
    for doc, score in rrf([[A, B, C], [B, D, A]]):
        print(doc.page_content, round(score, 5))
