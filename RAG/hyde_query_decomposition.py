# # rag-practice/hyde.py
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()  # .env থেকে GOOGLE_API_KEY load করে

# llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.3)

# hyde_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Write a short paragraph (3-4 sentences) that answers the question, "
#             "in the style of a research paper. Write in English. "
#             "Do not say you are unsure.",
#         ),
#         ("human", "{question}"),
#     ]
# )

# # Day 92-এর সেই prompt | llm | parser chain
# hyde_chain = hyde_prompt | llm | StrOutputParser()


# def generate_hypothetical_answer(question: str) -> str:
#     return hyde_chain.invoke({"question": question})


# if __name__ == "__main__":
#     q = "মডেল কীভাবে শব্দগুলোর মধ্যে সম্পর্ক বোঝে?"
#     print(generate_hypothetical_answer(q))


# # rag-practice/hyde_search.py
# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# from hyde import generate_hypothetical_answer  # 3a-র function

# load_dotenv()

# # ১. ছোট একটা demo collection (৪টা chunk, paper-এর style-এ)
# chunks = [
#     "The self-attention mechanism computes a weighted sum of value vectors, "
#     "where the weights come from the compatibility of queries and keys.",
#     "BERT is pretrained with masked language modeling, where random tokens "
#     "are hidden and the model predicts them from both directions.",
#     "Positional encodings are added to the input embeddings so the model "
#     "can use the order of tokens in a sequence.",
#     "Retrieval-augmented generation combines a retriever with a generator "
#     "to ground answers in external documents.",
# ]

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# db = Chroma.from_texts(chunks, embedding=embeddings)  # in-memory, demo-র জন্য

# # ২. একই প্রশ্ন, দুইভাবে search
# question = "How does the model understand relationships between words?"

# # (ক) সাধারণ search: প্রশ্ন সরাসরি
# plain = db.similarity_search_with_score(question, k=4)

# # (খ) HyDE search: আগে কাল্পনিক উত্তর, তারপর সেটা দিয়ে search
# fake_answer = generate_hypothetical_answer(question)
# hyde = db.similarity_search_with_score(fake_answer, k=4)

# # ৩. ফল দেখা (score = distance, ছোট মানে বেশি কাছের)
# print("=== সাধারণ search ===")
# for doc, score in plain:
#     print(f"{score:.3f} | {doc.page_content[:60]}")

# print("\n=== কাল্পনিক উত্তর ===")
# print(fake_answer)

# print("\n=== HyDE search ===")
# for doc, score in hyde:
#     print(f"{score:.3f} | {doc.page_content[:60]}")


# rag-practice/decompose.py
# from dotenv import load_dotenv
# from pydantic import BaseModel, Field
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()  # .env থেকে GOOGLE_API_KEY load করে


# # LLM-এর output-এর আকার: শুধু একটা string-এর list
# class SubQuestions(BaseModel):
#     sub_questions: list[str] = Field(
#         description="Self-contained sub-questions, 1 to 3 items"
#     )


# llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

# # structured output: LLM-কে বাধ্য করে SubQuestions-এর আকারে উত্তর দিতে
# structured_llm = llm.with_structured_output(SubQuestions)

# decompose_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Break the user's question into the smallest set of sub-questions "
#             "needed to answer it fully.\n"
#             "Rules:\n"
#             "1. Each sub-question must be self-contained: no 'it', 'this', 'that'. "
#             "Always repeat the subject by name.\n"
#             "2. Ask only what the user actually asked. Do not add background questions.\n"
#             "3. Write sub-questions in English.\n"
#             "4. Maximum 3 sub-questions.\n"
#             "5. If the question is already simple, return it unchanged as one item.",
#         ),
#         ("human", "{question}"),
#     ]
# )

# decompose_chain = decompose_prompt | structured_llm


# def decompose_question(question: str) -> list[str]:
#     result = decompose_chain.invoke({"question": question})
#     return result.sub_questions


# if __name__ == "__main__":
#     q = "ডায়াবেটিস রোগী কি ibuprofen খেতে পারে, আর কী কী side effect হয়?"
#     for i, sq in enumerate(decompose_question(q), start=1):
#         print(i, sq)


# rag-practice/decompose_search.py
# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# from decompose import decompose_question  # 6a-র function

# load_dotenv()

# # ১. Demo collection: ৬টা chunk, প্রতিটার নিজস্ব ID
# chunks = {
#     "bert_arch": "BERT uses a bidirectional Transformer encoder, so each token "
#     "attends to tokens on both its left and right.",
#     "gpt_arch": "GPT uses a unidirectional Transformer decoder, so each token "
#     "attends only to the tokens on its left.",
#     "bert_cls": "BERT performs strongly on classification tasks because its "
#     "bidirectional encoding captures full sentence context.",
#     "gpt_gen": "GPT is best suited for text generation, since it predicts "
#     "the next token from previous tokens.",
#     "pos_enc": "Positional encodings are added to the input embeddings so the "
#     "model can use the order of tokens.",
#     "rag": "Retrieval-augmented generation combines a retriever with a "
#     "generator to ground answers in external documents.",
# }

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# db = Chroma.from_texts(
#     texts=list(chunks.values()),
#     ids=list(chunks.keys()),  # fixed ID, তাই আবার run করলে duplicate হয় না
#     embedding=embeddings,
# )

# # ২. প্রশ্ন ভাঙো (6a)
# question = "BERT আর GPT-এর architecture-এ পার্থক্য কী, আর classification-এ কোনটা ভালো?"
# sub_questions = decompose_question(question)

# # ৩. প্রতিটা sub-question দিয়ে আলাদা search
# for sq in sub_questions:
#     print(f"\nSub-Q: {sq}")
#     results = db.similarity_search_with_score(sq, k=2)
#     for doc, score in results:
#         print(f"  {score:.3f} | {doc.page_content[:60]}")
