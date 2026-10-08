# from pathlib import Path
# from langchain_community.document_loaders import PyPDFLoader

# all_docs = []

# for pdf_path in Path("RAG").glob("*.pdf"):
#     loader = PyPDFLoader(pdf_path)
#     pages = loader.load()

#     for page in pages:
#         page.metadata["filename"] = pdf_path.name

#     all_docs.extend(pages)
# filenames = ["1706.pdf", "ML-1.pdf"]  # তোমার আসল নাম বসাও
# question = "How are Transformer and RAG related?"

# context_docs = []  # সব PDF-এর result এখানে জমবে

# for name in filenames:
#     retriever = vectorstore.as_retriever(
#         search_kwargs={"k": 2, "filter": {"filename": name}}  # প্রতি PDF থেকে ২টা
#     )
#     context_docs.extend(retriever.invoke(question))  # extend, কারণ invoke list দেয়

# for d in context_docs:
#     print(d.metadata["filename"], d.metadata["page"])

# print(len(all_docs))
# print({d.metadata["filename"] for d in all_docs})


"""
Day 120 - Multi-PDF (rag-practice/multi_pdf.py)

Pieces covered:
  1. Multi-PDF = same pipeline, but every chunk needs its identity
  2. Load many PDFs with a loop + metadata["filename"] + extend()
  3. ONE collection, metadata separates the PDFs
  4. Filter retrieval to a specific PDF
  5. Balanced retrieval (per-PDF k) so one PDF cannot take over top-k
  6. Citations with filename + page (page + 1)
  7. Deterministic IDs so re-ingesting does not create duplicates
"""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------- Config ----------
PDF_DIR = Path("RAG")  # যেখানে PDF গুলো আছে (নিজের path দাও)
PERSIST_DIR = "./chroma_db"  # Chroma এর data এখানে save হবে
COLLECTION_NAME = "papers_multi"  # একটাই collection (Piece 3)


# ---------- Piece 2: load many PDFs ----------
def load_all_pdfs(pdf_dir: Path):
    all_docs = []  # সব PDF এর সব page এখানে জমবে

    for pdf_path in sorted(pdf_dir.glob("*.pdf")):  # sorted = প্রতিবার একই order
        pages = PyPDFLoader(str(pdf_path)).load()  # এই PDF এর page এর list

        for page in pages:
            page.metadata["filename"] = pdf_path.name  # শুধু নাম, path না

        all_docs.extend(pages)  # flat list রাখতে extend

    return all_docs


# ---------- Chunking (Day 112 এর same setting) ----------
def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=40,
        separators=["\n\n", "\n", ". ", " ", ""],
        keep_separator="end",
    )
    return splitter.split_documents(docs)  # metadata প্রতিটা chunk এ কপি হয়


# ---------- Piece 7: deterministic IDs ----------
def make_ids(chunks):
    counters = {}  # {filename: এ পর্যন্ত কতটা chunk}
    ids = []
    for c in chunks:
        name = c.metadata["filename"]
        counters[name] = counters.get(name, 0) + 1
        ids.append(f"{name}_chunk{counters[name]}")  # যেমন "bert.pdf_chunk3"
    return ids


# ---------- Ingest (Piece 3 + 7) ----------
def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )


def ingest(vectorstore, chunks):
    ids = make_ids(chunks)
    # same id আবার এলে overwrite হয়, নতুন record হয় না
    vectorstore.add_documents(chunks, ids=ids)


# ---------- Piece 4: filter to a specific PDF ----------
def retrieve_from_one(vectorstore, question, filename, k=4):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k, "filter": {"filename": filename}}
    )
    return retriever.invoke(question)


# ---------- Piece 5: balanced retrieval across PDFs ----------
def retrieve_balanced(vectorstore, question, filenames, k_per_pdf=2):
    context_docs = []
    for name in filenames:
        context_docs.extend(retrieve_from_one(vectorstore, question, name, k=k_per_pdf))
    return context_docs


# ---------- Piece 6: citations ----------
def format_context(docs):
    # LLM কে দেওয়ার context: প্রতিটা chunk এর আগে [নম্বর] filename, page
    parts = []
    for i, d in enumerate(docs, start=1):
        name = d.metadata["filename"]
        page = d.metadata["page"] + 1  # PyPDFLoader এর page 0 থেকে শুরু
        parts.append(f"[{i}] {name}, page {page}\n{d.page_content}")
    return "\n\n".join(parts)


def build_sources(docs):
    # user কে দেখানোর list: {filename: [page, page]}
    sources = {}
    for d in docs:
        name = d.metadata["filename"]
        page = d.metadata["page"] + 1
        if name not in sources:
            sources[name] = []
        if page not in sources[name]:  # একই page দুইবার না
            sources[name].append(page)
    return sources


# ---------- Run everything ----------
def main():
    # Piece 2
    all_docs = load_all_pdfs(PDF_DIR)
    filenames = sorted({d.metadata["filename"] for d in all_docs})
    print(f"Pages loaded: {len(all_docs)} | PDFs: {filenames}")

    # Chunk + ingest (Piece 3, 7)
    chunks = chunk_docs(all_docs)
    print(f"Chunks: {len(chunks)}")

    vectorstore = get_vectorstore()
    ingest(vectorstore, chunks)
    # script দুইবার চালালেও এই সংখ্যা একই থাকার কথা (duplicate হয়নি তার প্রমাণ)
    print(f"Collection count: {vectorstore._collection.count()}")  # শুধু শেখার জন্য

    question = "How are Transformer and RAG related?"

    # Piece 4: শুধু প্রথম PDF এ খোঁজা
    only_one = retrieve_from_one(vectorstore, question, filenames[0], k=3)
    print(f"\n--- Only {filenames[0]} ---")
    print({d.metadata["filename"] for d in only_one})  # একটাই নাম আসার কথা

    # Piece 5: সাধারণ search (কোন PDF কতবার এলো দেখো)
    plain = vectorstore.as_retriever(search_kwargs={"k": 4}).invoke(question)
    print("\n--- Plain top-4 ---")
    print([d.metadata["filename"] for d in plain])

    # Piece 5: প্রতি PDF থেকে আলাদা করে
    balanced = retrieve_balanced(vectorstore, question, filenames, k_per_pdf=2)
    print("\n--- Balanced (k=2 per PDF) ---")
    print([d.metadata["filename"] for d in balanced])

    # Piece 6: citation
    print("\n--- Context for LLM ---")
    print(format_context(balanced))
    print("\n--- Sources for user ---")
    print(build_sources(balanced))


if __name__ == "__main__":
    main()
