# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# # 1. Load (Day 110)
# loader = PyPDFLoader("RAG/1706.pdf")
# pages = loader.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=300,
#     chunk_overlap=50,
#     separators=["\n\n", "\n", ". ", " ", ""],
#     keep_separator="end",
# )
# chunks = splitter.split_documents(pages)

# # 3. Vector store (তোমার আগের code)
# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vector_store = Chroma(
#     collection_name="vector_db_practice",
#     persist_directory="./chroma_db",
#     embedding_function=embedding,
# )

# # 4. ID বানানো: প্রতিটা chunk-এর নিজস্ব নাম
# ids = [f"attention_p{c.metadata['page']}_c{i}" for i, c in enumerate(chunks)]

# # 5. Insert
# vector_store.add_documents(documents=chunks, ids=ids)

# print("chunks:", len(chunks))
# print("stored:", vector_store._collection.count())


import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "How does attention work?"
texts = [
    "Attention lets the model focus on relevant words.",  # প্রাসঙ্গিক
    "RAG retrieves documents before generating an answer.",  # আংশিক প্রাসঙ্গিক
    "The cricket match was postponed due to rain.",  # অপ্রাসঙ্গিক
]

# query আর documents-এর জন্য আলাদা method
q = np.array(embeddings.embed_query(query))
vecs = [np.array(v) for v in embeddings.embed_documents(texts)]

# vector-এর দৈর্ঘ্য (norm)। 1.0-এর কাছাকাছি হলে normalized
print("query norm:", np.linalg.norm(q))


# তিনটা মাপ, Piece 1-3-র সূত্র হুবহু
def euclidean(a, b):
    return np.linalg.norm(a - b)


def dot(a, b):
    return np.dot(a, b)


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


print(f"\n{'text':<52} {'euclid':>7} {'dot':>7} {'cosine':>7}")
for t, v in zip(texts, vecs):
    print(f"{t[:50]:<52} {euclidean(q, v):7.3f} {dot(q, v):7.3f} {cosine(q, v):7.3f}")
