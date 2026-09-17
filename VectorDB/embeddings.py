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


# import chromadb

# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path="./chroma_db")

# default_ef = embedding_functions.DefaultEmbeddingFunction()

# collection = client.get_or_create_collection(
#     name="practice_day62",
#     embedding_function=default_ef,  # type: ignore
# )

# collection.add(
#     ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
#     documents=[
#         "I love eating pizza",
#         "Pasta is my favorite Italian food",
#         "I enjoy hiking in the mountains",
#         "Swimming is a great exercise",
#         "The stock market crashed today",
#     ],
# )

# result = collection.query(query_texts=["exercise and fitness"], n_results=1)

# print(result["documents"])
# print(result["distances"])


# import chromadb
# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path="./chroma_db")
# default_ef = embedding_functions.DefaultEmbeddingFunction()
# collection = client.get_or_create_collection(
#     name="practice_db", embedding_function=default_ef
# )

# collection.add(
#     documents=[
#         # --- Python exception handling related (relevant group) ---
#         "In Python, try and except blocks are used to catch and handle errors gracefully.",
#         "You can raise a custom exception in Python using the raise keyword with an Exception class.",
#         "The finally block in Python always executes, whether an exception occurred or not.",
#         "Using multiple except blocks lets you handle different error types separately in Python.",
#         # --- Completely unrelated topics (irrelevant group) ---
#         "The FIFA World Cup is held every four years and features the best football teams globally.",
#         "Heavy rainfall is expected this week due to a low-pressure system over the Bay of Bengal.",
#         "Biryani is a popular rice dish made with spices, meat, and aromatic basmati rice.",
#         "The new smartphone features a faster processor and improved battery life.",
#         "Cricket World Cup matches attract millions of viewers across South Asia.",
#         "A balanced diet includes proteins, carbohydrates, vitamins, and minerals.",
#     ],
#     ids=[
#         "doc1",
#         "doc2",
#         "doc3",
#         "doc4",
#         "doc5",
#         "doc6",
#         "doc7",
#         "doc8",
#         "doc9",
#         "doc10",
#     ],
# )


# def retrieve_with_threshold(collection, query_text, embed_fn, top_k, threshold):

#     result = collection.query(query_texts=[query_text], n_results=top_k)

#     documents = result["documents"][0]
#     distances = result["distances"][0]

#     print("RAW DISTANCES:", distances)

#     filtered_doc =[]
#     filtered_dis = []
#     for doc, dis in zip(documents,distances):
#         if dis <= threshold:
#             filtered_doc.append(doc)
#             filtered_dis.append(dis)

#     return filtered_doc, filtered_dis


# print(
#     retrieve_with_threshold(
#         collection, "how to handle errors in python code", default_ef, 10, 1
#     )
# )


# NITER Mini Retrieval System

# import chromadb
# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path= "./chroma_db")

# default_ef = embedding_functions.DefaultEmbeddingFunction()

# collection = client.get_or_create_collection(
#     name= "niter_info",
#     embedding_function= default_ef
# )
# collection.add(
#     documents = [
#         # --- NITER / CSE related (relevant group) ---
#         "NITER offers a Computer Science and Engineering program under the University of Dhaka.",
#         "The CSE department at NITER provides courses in programming, data structures, and software engineering.",
#         "Students at NITER can pursue elective courses such as Machine Learning, NLP, and Data Science.",
#         # --- Unrelated topics (irrelevant group) ---
#         "Messi and Ronaldo are considered two of the greatest football players in history.",
#         "A good cup of tea requires boiling water and steeping the tea leaves for a few minutes.",
#         "Dhaka experiences heavy traffic congestion during office hours on weekdays.",
#         "The latest action movie broke box office records in its opening weekend.",
#         "Regular exercise and a balanced diet contribute to better physical health.",
#     ],

#     ids = ["niter1", "niter2", "niter3", "misc1", "misc2", "misc3", "misc4", "misc5"]
# )

# def retrieve_with_threshold(collection, query_text, top_k, threshold):

#     result = collection.query(
#         query_texts = [query_text],
#         n_results = top_k
#     )
#     documents = result["documents"][0]
#     distances = result["distances"][0]

#     print("Raw distances: ", distances)

#     filtered_documents = []
#     filtered_distances = []

#     for dis, doc in zip(distances, documents):
#         if dis <= threshold:
#             filtered_distances.append(dis)
#             filtered_documents.append(doc)

#     return filtered_distances, filtered_documents

# print(retrieve_with_threshold(collection, "what courses does the CSE department offer", 8, 1.3))


# import chromadb
# import tiktoken
# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path= "./chroma_db")
# default_ef = embedding_functions.DefaultEmbeddingFunction()
# collection = client.get_or_create_collection(
#     name= "practice_chunk",
#     embedding_function= default_ef
# )
# encoding = tiktoken.get_encoding("cl100k_base")

# text = """The CSE department at NITER has a fixed deadline for thesis submission every year, usually around mid-December. If a student cannot submit on time, they must get written permission from their supervisor to request an extension. Extensions are typically granted for up to one week, but this depends on the department head's approval. If someone still cannot submit even after the extension, they will have to enroll again in the next semester."""

# tokens = encoding.encode(text)
# print(tokens)
# print(len(tokens))
# back_to_text = encoding.decode(tokens)
# print(back_to_text)

# bangla_text = "ami tomake bhalobashi"
# english_text = "I love AI"

# bangla_tokens = encoding.encode(bangla_text)
# english_tokens = encoding.encode(english_text)

# print(f"Bangla: {len(bangla_tokens)} tokens for {len(bangla_text)} characters")
# print(f"English: {len(english_tokens)} tokens for {len(english_text)} characters")

# # def fixed_chunk_size(text:str, chunk_size:int, overlap:int) -> list:

# #     chunk = []
# #     start = 0

# #     while start < len(text):
# #         end = start + chunk_size
# #         chunk.append(text[start:end])
# #         start = end-overlap

# #     return chunk

# # print(fixed_chunk_size(text,50, 0))


# import tiktoken

# encoding = tiktoken.get_encoding("cl100k_base")

# text = """The CSE department at NITER has a fixed deadline for thesis submission every year, usually around mid-December. If a student cannot submit on time, they must get written permission from their supervisor to request an extension. Extensions are typically granted for up to one week, but this depends on the department head's approval. If someone still cannot submit even after the extension, they will have to enroll again in the next semester."""


# def token_based_chunk(text, chunk_size, overlap):
#     chunk = []
#     start = 0
#     tokens = encoding.encode(text)

#     while start < len(tokens):
#         end = start + chunk_size
#         token_slice = tokens[start:end]
#         decode_token = encoding.decode(token_slice)
#         chunk.append(decode_token)
#         start = end - overlap

#     return chunk

# print(token_based_chunk(text, 50, 10))


# import tiktoken

# encoding = tiktoken.get_encoding("cl100k_base")

# text = """The CSE department at NITER has a fixed deadline for thesis submission every year, usually around mid-December. If a student cannot submit on time, they must get written permission from their supervisor to request an extension. Extensions are typically granted for up to one week, but this depends on the department head's approval. If someone still cannot submit even after the extension, they will have to enroll again in the next semester."""


# # def sentence_chunk(text):
# #     sentences = text.split(".")
# #     print(len(sentences))
# #     word = 0
# #     chunk = ""
# #     for i in sentences:
# #         if word < 15:
# #             word += sentences
# #         chunk.append(word)
# #     return chunk

# # print(sentence_chunk(text))


# def paragraph_chunk(text: str, word_limit: int) -> list:
#     paragraphs = text.split("\n\n")

#     chunks = []
#     current_chunk = ""
#     current_word_count = 0

#     for paragraph in paragraphs:
#         paragraph = paragraph.strip()
#         if paragraph == "":
#             continue

#         paragraph_word_count = len(paragraph.split())

#         if current_word_count + paragraph_word_count > word_limit:
#             chunks.append(current_chunk.strip())
#             current_chunk = paragraph + "\n\n"
#             current_word_count = paragraph_word_count
#         else:
#             current_chunk += paragraph + "\n\n"
#             current_word_count += paragraph_word_count

#     if current_chunk != "":
#         chunks.append(current_chunk.strip())

#     return chunks

# print(paragraph_chunk(text, 30))


# import chromadb
# from chromadb.utils import embedding_functions

# client = chromadb.PersistentClient(path="./chroma_db")
# default_ef = embedding_functions.DefaultEmbeddingFunction()
# collection = client.get_or_create_collection(
#     name="metadata_filtering", embedding_function=default_ef
# )

# # collection.add(
# #     ids=["1", "2", "3", "4", "5"],
# #     documents=[
# #         "Newton's second law states F = ma",
# #         "Water boils at 100 degrees Celsius",
# #         "Python is an interpreted language",
# #         "Gravity causes objects to fall",
# #         "For loops iterate over sequences",
# #     ],
# #     metadatas=[
# #         {"topic": "Physics"},
# #         {"topic": "Chemistry"},
# #         {"topic": "Programming"},
# #         {"topic": "Physics"},
# #         {"topic": "Programming"},
# #     ],
# # )
# collection.upsert(
#     ids = ["1", "2", "3", "4", "5", "6"],

#     documents = [
#         "Newton's second law states F = ma",
#         "Water boils at 100 degrees Celsius",
#         "Python is an interpreted language",
#         "Gravity causes objects to fall",
#         "For loops iterate over sequences",
#         "Photosynthesis converts sunlight into energy",
#     ],

#     metadatas = [
#         {
#             "topic": "Physics",
#             "source": "textbook",
#             "user_id": "userA",
#             "date": "2026-01-15",
#         },
#         {"topic": "Chemistry", "source": "notes", "user_id": "userB", "date": "2026-03-02"},
#         {
#             "topic": "Programming",
#             "source": "textbook",
#             "user_id": "userA",
#             "date": "2026-05-10",
#         },
#         {"topic": "Physics", "source": "notes", "user_id": "userB", "date": "2026-02-20"},
#         {
#             "topic": "Programming",
#             "source": "notes",
#             "user_id": "userA",
#             "date": "2026-06-01",
#         },
#         {
#             "topic": "Biology",
#             "source": "textbook",
#             "user_id": "userB",
#             "date": "2026-04-18",
#         },
#     ]
# )

# # result = collection.query(
# #     query_texts=["What is newton second law"],
# #     n_results=3,
# #     where={"$or": [{"topic": "Physics"}, {"source": "textbook"}]},
# # )
# # print(result["documents"])
# # result = collection.query(
# #     query_texts=["What is newton second law"],
# #     n_results=3,
# #     where={"$and": [{"topic": "Physics"}, {"source": "textbook"}]},
# # )
# # print(result["documents"])

# # result = collection.query(
# #     query_texts=["What is newton second law"],
# #     n_results=3,
# #     where={"date": {"$gt": "2026-04-18"}},
# # )
# # print(result["documents"])


# result = collection.query(
#     query_texts=["Newtons law"],
#     n_results= 3,
#     where= {
#         "$and": [{"source": "textbook"}, {"topic": {"$ne": "Biology"}}]}
# )
# print(result["documents"])


# import chromadb

# client = chromadb.PersistentClient(path= "./chroma_db")
# collection = client.get_or_create_collection(name= "niter_db")

# query_text = "NITER এ কি কি CSE course আছে"

# results = collection.query(
#     query_texts= [query_text],
#     n_results= 3,
# )
# candidate_docs = results["documents"][0]
# print("Stage 1 (retrieval) order:")

# for dis, doc in enumerate (candidate_docs):
#     print(dis, doc[:60])

from sentence_transformers import CrossEncoder

# একটা pretrained cross-encoder model লোড করছি
# এই model বিশেষভাবে "query-document relevance scoring"-এর জন্য train করা
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# Cross-encoder-কে pair বানিয়ে দিতে হয়: [query, document] — প্রতিটা candidate-এর জন্য
pairs = [[query_text, doc] for doc in candidate_docs]

# predict() প্রতিটা pair-কে একসাথে দেখে একটা relevance score বের করে
scores = reranker.predict(pairs)

print("\nRaw cross-encoder scores:")
for doc, score in zip(candidate_docs, scores):
    print(round(score, 3), "-", doc[:60])

# score আর document একসাথে zip করে, score অনুযায়ী descending sort
reranked = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)

print("\nStage 2 (reranked) order:")
for doc, score in reranked:
    print(round(score, 3), "-", doc[:60])
