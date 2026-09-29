# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("RAG/1.pdf").load()

# for doc in loader:
#     content = doc.page_content.lower()

#     count = content.count("attention")

#     print(content)
#     print("Count:", count)
#     print("Page:", doc.metadata["page"] + 1)


# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("RAG/ML-1.pdf")
# docs = loader.load()

# print(len(docs))
# print(docs[3].page_content)
# print(docs[0].metadata)


from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_file(path):
    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)
    elif path.endswith(".txt", ".md"):
        loader = TextLoader(path, encoding="utf-8")
    else:
        print("এই type চলবে না")
        return None

    return loader.load()


docs = load_file("RAG/ML-1.pdf")

if docs:
    print(len(docs))
    print(docs[3].page_content)
    print(docs[0].metadata)
