from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma(
    collection_name="my_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)

results = vectorstore.similarity_search_with_score("what is my name", k=3)
for doc, score in results:
    print("score   :", score)
    print("metadata:", doc.metadata)
    print("text    :", doc.page_content[:200])
    print("-" * 40)
