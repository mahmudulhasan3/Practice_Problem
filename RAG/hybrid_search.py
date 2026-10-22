# Setup (একবার): pip install rank_bm25 langchain-community langchain-chroma langchain-huggingface
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from rrf import rrf

load_dotenv()

# ---------- 1) PDF load (path তোমার আসল path দিয়ে বদলাও) ----------
loader = PyPDFLoader("RAG/1706.pdf")
pages = loader.load()

# ---------- 2) Chunk (একটাই list, দুই retriever-এর জন্য) ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=40,
    separators=["\n\n", "\n", ". ", " ", ""],
    keep_separator="end",
)
chunks = splitter.split_documents(pages)
print("Total chunks:", len(chunks))


# ---------- 3) BM25 retriever ----------
def preprocess(text):
    words = text.lower().split()  # ছোট হাতের + শব্দে ভাঙা
    return [w.strip(".,;:()[]\"'") for w in words]  # দুই প্রান্তের চিহ্ন কাটা


bm25 = BM25Retriever.from_documents(chunks, k=10, preprocess_func=preprocess)

# ---------- 4) Dense retriever ----------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="hybrid_demo",
)
dense = vectorstore.as_retriever(search_kwargs={"k": 10})


# ---------- 5) Hybrid search ----------
def hybrid_search(query, final_k=3):
    bm25_results = bm25.invoke(query)
    dense_results = dense.invoke(query)
    fused = rrf([dense_results, bm25_results])  # [(doc, score), ...]
    return fused[:final_k]


# ---------- 6) Test ----------
queries = [
    "BLEU 28.4",
    "multi-head attention",
    "how does the model look at all words at once",
]

for query in queries:
    print("=" * 60)
    print("QUERY:", query)

    for i, (doc, score) in enumerate(hybrid_search(query), start=1):
        print(f"--- Result {i} | page {doc.metadata['page'] + 1} | rrf={score:.5f} ---")
        print(doc.page_content[:150])
