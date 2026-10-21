import os
import time

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# ---------- Config ----------
PDF_PATH = "data/papers/1706.03762v7.pdf"  # তোমার PDF-এর path
PERSIST_DIR = "chroma_exp"  # experiment-এর জন্য আলাদা folder
K = 5  # top-k

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# ---------- Test set: প্রশ্ন + evidence phrase ----------
# এখানে ১০-১৫টা পর্যন্ত বাড়াও (নিজে paper পড়ে বানাও)
test_set = [
    {
        "question": "Transformer-এ কয়টা parallel attention head ব্যবহার হয়েছে?",
        "evidence": "h = 8 parallel attention layers",
    },
    {
        "question": "Positional encoding কেন দরকার?",
        "evidence": "inject some information about the relative or absolute position",
    },
    {
        "question": "Encoder-এ কয়টা identical layer আছে?",
        "evidence": "a stack of N = 6 identical layers",
    },
]


# ---------- Step 1: Hit চেক ----------
def normalize(text: str) -> str:
    # whitespace সমান করো + ছোট হাতের অক্ষর
    return " ".join(text.split()).lower()


def is_hit(evidence: str, retrieved_chunks: list[str]) -> bool:
    evidence = normalize(evidence)
    for chunk in retrieved_chunks:
        if evidence in normalize(chunk):
            return True
    return False


# ---------- Step 2: Hit Rate ----------
def hit_rate(test_set: list[dict], retrieve_fn, k: int = K) -> float:
    hits = 0
    for item in test_set:
        retrieved = retrieve_fn(item["question"], k)
        if is_hit(item["evidence"], retrieved):
            hits += 1
    return hits / len(test_set)


# ---------- PDF একবারই load ----------
pages = PyPDFLoader(PDF_PATH).load()


def check_evidence_exists():
    # sanity check: evidence phrase আদৌ PDF-এর text-এ আছে কিনা
    full_text = normalize(" ".join(p.page_content for p in pages))
    for item in test_set:
        if normalize(item["evidence"]) not in full_text:
            print(f"⚠️  Evidence PDF-এ পাওয়া যায়নি: {item['evidence']}")


# ---------- Step 3: প্রতিটা config-এর জন্য নতুন collection ----------
def build_retrieve_fn(chunk_size: int, chunk_overlap: int):
    # ১. split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(pages)

    # ২. পুরনো collection মুছে নতুন বানাও (নইলে chunk মিশে যাবে)
    name = f"exp_{chunk_size}_{chunk_overlap}"
    try:
        Chroma(
            collection_name=name,
            embedding_function=embeddings,
            persist_directory=PERSIST_DIR,
        ).delete_collection()
    except Exception:
        pass  # collection আগে ছিল না

    store = Chroma(
        collection_name=name,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )

    # ৩. ছোট batch-এ insert (free tier rate limit এড়াতে)
    batch_size = 50
    for i in range(0, len(chunks), batch_size):
        store.add_documents(chunks[i : i + batch_size])
        time.sleep(1)

    # ৪. retrieve function
    def retrieve(question: str, k: int) -> list[str]:
        docs = store.similarity_search(question, k=k)
        return [d.page_content for d in docs]

    # chunk সংখ্যা আর গড় আকারও ফেরত দিচ্ছি (শুধু score দেখে ঠকে না যেতে)
    avg_len = sum(len(c.page_content) for c in chunks) // len(chunks)
    return retrieve, len(chunks), avg_len


def run_experiment(configs: list[tuple]) -> list[tuple]:
    results = []
    print(f"{'size':<6}{'overlap':<9}{'chunks':<8}{'avg_len':<9}{'HitRate'}")
    for size, overlap in configs:
        retrieve_fn, n_chunks, avg_len = build_retrieve_fn(size, overlap)
        score = hit_rate(test_set, retrieve_fn)
        results.append((size, overlap, score))
        print(f"{size:<6}{overlap:<9}{n_chunks:<8}{avg_len:<9}{score:.2f}")
    return results


def pick_best(results: list[tuple]) -> tuple:
    # সবচেয়ে বেশি score; সমান হলে ছোট size (ছোট chunk = কম noise, কম token)
    best_score = max(r[2] for r in results)
    top = [r for r in results if r[2] == best_score]
    return min(top, key=lambda r: r[0])


if __name__ == "__main__":
    check_evidence_exists()

    print("\n=== ধাপ ক: overlap=50 fixed, size বদলাচ্ছে ===")
    size_results = run_experiment([(300, 50), (500, 50), (800, 50), (1200, 50)])
    best_size, _, _ = pick_best(size_results)
    print(f"\n✅ সেরা size: {best_size}")

    print(f"\n=== ধাপ খ: size={best_size} fixed, overlap বদলাচ্ছে ===")
    overlap_results = run_experiment(
        [(best_size, 0), (best_size, 50), (best_size, 100), (best_size, 150)]
    )
    final = pick_best(overlap_results)
    print(
        f"\n🏆 সেরা config: size={final[0]}, overlap={final[1]}, HitRate={final[2]:.2f}"
    )
