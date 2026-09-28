from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("RAG/1.pdf").load()

for doc in loader:
    content = doc.page_content.lower()

    count = content.count("attention")

    print(content)
    print("Count:", count)
    print("Page:", doc.metadata["page"] + 1)
