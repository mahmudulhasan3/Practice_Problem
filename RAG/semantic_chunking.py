# from langchain_community.document_loaders import PyPDFLoader
# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# splitter = SemanticChunker(
#     embedding,
#     breakpoint_threshold_type="percentile",
#     breakpoint_threshold_amount=95
# )
# docs = PyPDFLoader("RAG/1706.pdf").load()

# chunks = splitter.split_documents(docs)

# print("Total chunks:", len(chunks))
# lengths = [len(c.page_content) for c in chunks]
# print("Min length:", min(lengths), "| Max length:", max(lengths))


# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# from langchain_core.stores import InMemoryStore
# from langchain_classic.retrievers import ParentDocumentRetriever

# # 1. Document load (আগের মতোই)
# docs = PyPDFLoader("RAG/1706.pdf").load()

# # 2. Embedding model (local)
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# # 3. দুই স্তরের splitter
# parent_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1500, chunk_overlap=100
# )  # বড়
# child_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)  # ছোট

# # 4. দুইটা আলাদা জায়গা
# vectorstore = Chroma(
#     collection_name="parent_child_practice",
#     embedding_function=embeddings,
# )  # এখানে শুধু Child + embedding যাবে
# docstore = InMemoryStore()  # এখানে Parent text থাকবে (embedding নেই)

# # 5. Retriever বানাও
# retriever = ParentDocumentRetriever(
#     vectorstore=vectorstore,
#     docstore=docstore,
#     child_splitter=child_splitter,
#     parent_splitter=parent_splitter,
# )

# # 6. Ingestion: split + child embed + parent store + parent_id জোড়া, সব এই এক লাইনে
# retriever.add_documents(docs)

# # 7. তুলনা: Child বনাম Parent
# query = "What is self-attention?"

# children = vectorstore.similarity_search(query, k=3)  # শুধু Child খোঁজা
# parents = retriever.invoke(query)  # Child দিয়ে খুঁজে Parent ফেরত

# print("Children:", [len(c.page_content) for c in children])
# print("Parents: ", [len(p.page_content) for p in parents])


from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.stores import InMemoryStore

docs = PyPDFLoader("RAG/1706.pdf").load()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1300, chunk_overlap=150,)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

vectorstore = Chroma(
    embedding_function=embedding, collection_name="practice_collection"
)

docstore = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    parent_splitter=parent_splitter,
    child_splitter=child_splitter,
)

retriever.add_documents(docs)
query = "What is attention?"

child = vectorstore.similarity_search(query= query, k= 5)
parent = retriever.invoke(query)

print("Children:", [len(c.page_content) for c in child])
print("Parents: ", [len(p.page_content) for p in parent])
