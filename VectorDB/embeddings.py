# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

# result = client.models.embed_content(
#     model = "gemini-embedding-001",
#     contents = "I like dog",
#     config = {"task_type":"RETRIVAL-DOCUMENT"}
# )

# vector = result.embeddings[0].values
# print(f"Vector-এর প্রথম 5টা সংখ্যা: {vector[:5]}")
# print(f"Vector-এ মোট কতগুলো সংখ্যা আছে (Dimension): {len(vector)}")


# from google import genai
# from dotenv import load_dotenv
# import os
# from google.genai import types

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# chunks = [
#     "Dhaka is the capital of Bangladesh.",
#     "NITER is affiliated with the University of Dhaka.",
#     "FastAPI is a modern Python web framework.",
# ]
# doc_embedding = client.models.embed_content(
#     model="gemini-embedding-001",
#     contents= chunks,
#     config=types.EmbedContentConfig(
#         output_dimensionality=400, task_type="RETRIEVAL_DOCUMENT"
#     ),
# )

# for i, emb in enumerate(doc_embedding.embeddings):
#     print(f"Chunk: {i}, {chunks[i][:5]}, len: {len(emb.values)}")


# from google import genai
# from dotenv import load_dotenv
# from google.genai import types
# import os

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# sentences = [
#     "The cat is sleeping on the sofa.",
#     "A dog is playing in the garden.",
#     "My cat loves to chase mice at night.",
#     "FastAPI is a modern Python web framework for building APIs.",
#     "Python's async support makes FastAPI very fast.",
# ]
# response = client.models.embed_content(
#     model= "gemini-embedding-001",
#     contents= sentences,
#     config= types.EmbedContentConfig(
#         output_dimensionality= 256
#     )
# )
# for i, emb in enumerate(response.embeddings):
#     print(f"chunk: {i}, {sentences[i]}, {len(emb.values)}")


# import chromadb
# from chromadb.utils import embedding_functions
# import os
# from dotenv import load_dotenv

# load_dotenv()

# google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# client = chromadb.PersistentClient(path="./chroma_db")

# collection = client.get_or_create_collection(
#     name="university_docs", embedding_function=google_ef
# )

# collection.add(
#     documents=[
#         "Students must attend 75% classes to sit for final exams.",
#         "The library is open from 8 AM to 10 PM.",
#     ],
#     ids=["doc1", "doc2"],
# )
# print("✅ Added successfully")


# import chromadb
# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()


# # আমাদের নিজের Embedding Function — ChromaDB-কে বলে দিচ্ছি
# # text থেকে vector কীভাবে বানাতে হবে
# class GeminiEmbeddingFunction:
#     def __init__(self):
#         self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#     # ChromaDB internally এই method-টাই কল করবে
#     def __call__(self, input):
#         # input হলো text-এর একটা list, প্রতিটার embedding বানাতে হবে
#         result = self.client.models.embed_content(
#             model="gemini-embedding-001",  # embedding-এর জন্য আলাদা model
#             contents=input,
#         )
#         # প্রতিটা embedding-এর শুধু values (numbers-এর list) বের করে দিচ্ছি
#         return [e.values for e in result.embeddings]


# gemini_ef = GeminiEmbeddingFunction()

# client = chromadb.PersistentClient(path="./chroma_db")

# collection = client.get_or_create_collection(
#     name="university_docs", embedding_function=gemini_ef
# )

# collection.add(
#     documents=[
#         "Students must attend 75% classes to sit for final exams.",
#         "The library is open from 8 AM to 10 PM.",
#     ],
#     ids=["doc1", "doc2"],
# )

# print("✅ Added successfully")

# from google import genai
# from dotenv import load_dotenv
# import os
# import chromadb

# client = chromadb.PersistentClient(path= "./chroma_db")

# collection = client.get_or_create_collection(name= "university_docs")

# collection.add(
#     documents=[
#         "Students must attend 75% classes to sit for final exams.",
#         "The library is open from 8 AM to 10 PM.",
#     ],
#     ids= ["doc1","doc2"]
# )
# result = collection.get(ids=["doc2"])
# print(result)
# collection.update(
#     ids= ["doc2"],
#     documents= "I am mahmud"
# )
# print(collection.get(ids = ["doc2"]))
# now = collection.delete(ids = ["doc2"])
# print(collection.get(ids=["doc2"]))


# collection.upsert(
#     ids = ["doc2", "doc4"],
#     documents=[
#         "I am mahmud",
#         "WHat is ai"
#     ]
# )
# print(collection.get(ids=["doc2"]))
# print(collection.get(ids=["doc4"]))


# import chromadb

# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="my_notes")

# collection.upsert(
#     ids=["doc1", "doc2"],
#     documents=["Hello, I am Mahmud Hasan", "ID: CS-2203009"],
#     metadatas=[
#         {"topic": "introduction", "source": "presonal_notes"},
#         {"topic": "introduction", "source": "presonal_notes"},
#     ],
# )
# result = collection.get(ids=["doc1"])
# print(result)

# print(collection.get(where= {"topic": "introduction"}))


# import chromadb

# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="personal_kb")

# collection.add(
#     ids=["kb_1", "kb_2", "kb_3", "kb_4", "kb_5"],
#     documents=[
#         "NITER CSE",
#         "Attendance minimum 75%",
#         "Library open 8AM-10PM",
#         "ID: CS-2203009",
#         "AI/LLM Engineer",
#     ],
#     metadatas=[
#         {"topic": "education", "source": "personal"},
#         {"topic": "academic_rule", "source": "university_docs"},
#         {"topic": "academic_rule", "source": "university_docs"},
#         {"topic": "personal_info", "source": "personal"},
#         {"topic": "career_goal", "source": "personal"},
#     ],
# )

# print(collection.get(ids=["kb_1"]))

# print(collection.get(where={"topic": "academic_rule"}))

# collection.update(ids=["kb_1"], documents=["NITER CSE 4th year"])

# print(collection.get(ids=["kb_1"]))

# collection.upsert(
#     ids=["kb_1", "kb_6"],
#     documents=["NITER CSE", "Who are you"],
#     metadatas=[
#         {"topic": "education", "source": "personal"},
#         {"topic": "introduction", "source": "personal"},
#     ],
# )

# print(collection.get(ids=["kb_1", "kb_6"]))

# collection.delete(ids=["kb_6"])

# print(collection.get(ids=["kb_6"]))


# def print_all_document(collection):
#     result = collection.get()
#     for ids, documents, metadatas in zip(
#         result["ids"], result["documents"], result["metadatas"]
#     ):
#         print(f"ID: {ids}")
#         print(f"Text: {documents}")
#         print(f"Metadata: {metadatas}")
#         print("-" * 40)


# print_all_document(collection)


# import chromadb
# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path="./chroma_db")

# default_ef = embedding_functions.DefaultEmbeddingFunction()

# collection = client.get_or_create_collection(
#     name="practice_b",
#     embedding_function=default_ef,
# )

# collection.add(
#     documents=[
#         "I love playing football",
#         "I enjoy playing soccer",
#         "The weather is very cold today",
#     ],
#     ids=["doc1", "doc2", "doc3"],
# )

# result = collection.query(query_texts=["I love football"], n_results=3)

# print(result["ids"])
# print(result["documents"])
# print(result["distances"])

# result = collection.query(
#     query_texts=["I love playing football"],  # doc1-এর সাথে হুবহু মিল
#     n_results=1,
# )

# print(result["distances"])


import chromadb

from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")

default_ef = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="practice_day62",
    embedding_function=default_ef,  # type: ignore
)

collection.add(
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
    documents=[
        "I love eating pizza",
        "Pasta is my favorite Italian food",
        "I enjoy hiking in the mountains",
        "Swimming is a great exercise",
        "The stock market crashed today",
    ],
)

result = collection.query(query_texts=["exercise and fitness"], n_results=1)

print(result["documents"])
print(result["distances"])
