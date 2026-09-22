from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
client.delete_collection(name="niter_info")  


embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = Chroma(
    collection_name="niter_info",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)
vectorstore.add_texts(
    texts=["তোমার NITER সম্পর্কিত chunk text এখানে...", "আরেকটা chunk..."],
    metadatas=[{"source": "..."}, {"source": "..."}],
    ids=["doc1", "doc2"],
)
# retriever = vectorestore.as_retriever(
#     search_type="similarity_score_threshold",
#     search_kwargs={"k": 3, "score_threshold": 0.7},
# )

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3},
)

results = retriever.invoke("NITER CSE admission requirements")

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
