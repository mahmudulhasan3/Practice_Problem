# # Setup (একবার): pip install rank_bm25 langchain-community
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.retrievers import BM25Retriever

# # 1) PDF load (path তোমার আসল path দিয়ে বদলাও)
# loader = PyPDFLoader("RAG/1706.pdf")
# pages = loader.load()

# # 2) Chunk (Day 112-এর settings)
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=300,
#     chunk_overlap=40,
#     separators=["\n\n", "\n", ". ", " ", ""],
#     keep_separator="end",
# )
# chunks = splitter.split_documents(pages)

# # 3) BM25 index বানানো + retriever তৈরি
# bm25 = BM25Retriever.from_documents(chunks, k=3)

# # 4) Search
# query = [
#     "BLEU 28.4",
#     "multi-head attention",
#     "how does the model look at all words at once",
# ]

# for i in query:
#     results = bm25.invoke(i)

# for i, doc in enumerate(results, start=1):
#     print(f"--- Result {i} | page {doc.metadata['page'] + 1} ---")
#     print(doc.page_content)


# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# load_dotenv()

# # 3b) Dense retriever (একই chunks, MiniLM embedding)
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vectorstore = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     collection_name="hybrid_demo",  # নতুন নাম, পুরোনো collection-এর সাথে মিশবে না
# )

# dense = vectorstore.as_retriever(search_kwargs={"k": 3})

# for i in query:
#     dense_results = dense.invoke(i)

# print("\n>>> DENSE")
# for i, doc in enumerate(dense_results, start=1):
#     print(f"--- Result {i} | page {doc.metadata['page'] + 1} ---")
#     print(doc.page_content[:150])


# from langchain_core.documents import Document


# def rrf(result_lists, k=60):
#     scores = {}  # key -> মোট RRF score
#     docs = {}  # key -> আসল Document (পরে ফেরত দেওয়ার জন্য)

#     for results in result_lists:  # প্রতিটা retriever-এর list
#         for rank, doc in enumerate(results, start=1):  # rank 1 থেকে শুরু
#             key = make_key(doc)
#             docs[key] = doc
#             scores[key] = scores.get(key, 0) + 1 / (k + rank)

#     # score বড় থেকে ছোট সাজানো
#     ranked_keys = sorted(scores, key=scores.get, reverse=True)
#     return [(docs[key], scores[key]) for key in ranked_keys]


# def fake(name):
#     return Document(page_content=name, metadata={"source": "x.pdf", "page": 0})


# A, B, C, D = fake("A"), fake("B"), fake("C"), fake("D")

# dense_list = [A, B, C]  # Dense ranking
# bm25_list = [B, D, A]  # BM25 ranking

# for doc, score in rrf([dense_list, bm25_list]):
#     print(doc.page_content, round(score, 5))


# from rrf import rrf


# def hybrid_search(query, final_k=3):
#     bm25_results = bm25.invoke(query)
#     dense_results = dense.invoke(query)
#     fused = rrf([dense_results, bm25_results])  # [(doc, score), ...]
#     return fused[:final_k]  # শুধু top final_k


# queries = [
#     "BLEU 28.4",
#     "multi-head attention",
#     "how does the model look at all words at once",
# ]

# for query in queries:
#     print("=" * 60)
#     print("QUERY:", query)

#     for i, (doc, score) in enumerate(hybrid_search(query), start=1):
#         print(f"--- Result {i} | page {doc.metadata['page'] + 1} | rrf={score:.5f} ---")
#         print(doc.page_content[:150])



