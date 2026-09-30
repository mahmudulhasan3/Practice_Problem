from langchain_community.document_loaders import PyPDFLoader
docs = PyPDFLoader("RAG/ML-1.pdf").load()

for doc in docs:
    doc.metadata["product"] = "Attention Is All You Need"

print(docs[0].metadata)
print(docs[2].page_content[:200])
