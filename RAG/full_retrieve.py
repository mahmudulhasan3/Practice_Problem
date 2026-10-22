from hybrid_search import hybrid_search  # Day 128-এর file ও function
from rerank_fn import rerank  # Piece 3-এর file ও function


def retrieve(question, candidates=10, final_k=3):
    # ধাপ ১: hybrid দিয়ে বড় candidate pool
    candidate_docs = hybrid_search(question, final_k=candidates)

    # ধাপ ২: reranker দিয়ে সেরা final_k টা
    top_docs = rerank(question, candidate_docs, top_n=final_k)

    return top_docs


# if __name__ == "__main__":
#     question = "What is multi-head attention?"

#     print("=== Hybrid only (top-3) ===")
#     for doc in hybrid_search(question, final_k=3):
#         print(doc.metadata.get("page"), "|", doc.page_content[:70])

#     print("\n=== Hybrid + Rerank (top-3) ===")
#     for doc in retrieve(question):
#         print(doc.metadata.get("page"), "|", doc.page_content[:70])
