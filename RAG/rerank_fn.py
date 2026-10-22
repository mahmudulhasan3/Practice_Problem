from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

# app start-এ একবার load (প্রতি call-এ না)
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(question, docs, top_n=3):
    # ধাপ ১: (question, text) জোড়া
    pairs = [(question, doc.page_content) for doc in docs]

    # ধাপ ২: প্রতিটা জোড়ার score
    scores = reranker.predict(pairs)

    # ধাপ ৩: (score, doc) জোড়া
    scored = list(zip(scores, docs))

    # ধাপ ৪: বড় score আগে
    scored.sort(key=lambda item: item[0], reverse=True)

    # ধাপ ৫: শুধু doc, প্রথম top_n টা
    return [doc for score, doc in scored[:top_n]]

docs = [
    Document(
        page_content="The Transformer was trained on the WMT 2014 English-German dataset.",
        metadata={"filename": "attention.pdf", "page": 7},
    ),
    Document(
        page_content="Multi-head attention runs several attention functions in parallel, "
        "letting the model attend to information from different positions.",
        metadata={"filename": "attention.pdf", "page": 4},
    ),
    Document(
        page_content="Rice is the main crop in Bangladesh and grows best in monsoon season.",
        metadata={"filename": "agri.pdf", "page": 1},
    ),
]

question = "What is multi-head attention?"

result = rerank(question, docs, top_n=2)

for doc in result:
    print(doc.metadata, "|", doc.page_content[:50])
