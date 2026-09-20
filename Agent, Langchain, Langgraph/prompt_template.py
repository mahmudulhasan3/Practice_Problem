# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os

# load_dotenv()


# model = ChatGoogleGenerativeAI(
#     model = "gemini-3.1-flash-lite",
#     google_api_key = os.getenv("GEMINI_API_KEY"),
#     temperature = 0.7
# )

# def response_txt(response):
#     if isinstance(response.content, list):
#         return response.content[0]['text']
#     else:
#         return response.content

# prompt_template = ChatPromptTemplate.from_template("Summarize this: {text}")

# final_prompt = prompt_template.invoke(
#     {"text": "FastAPI is a modern Python web framework"}
# )
# response = model.invoke(final_prompt)
# text = response_txt(response)
# print(text)

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # prompt = ChatPromptTemplate.from_template(
# #     "Explain {topic} in simple terms for a {level} student."
# # )
# # final_prompt = prompt.format(topic="recursion", level="beginner")

# # print(final_prompt)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful {subject} tutor."),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ]
# )
# final_prompt = prompt.format_messages(
#     chat_history=[
#         ("human", "What is Python?"),
#         ("ai", "Python is a programming language."),
#     ],
#     question="Is it good for beginners?",
#     subject = "ICT"
# )

# print(final_prompt)


# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a senior software engineer mentor."),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ]
# )

# fake_history = [
#     ("human", "My name is Mahmud."),
#     ("ai", "Nice to meet you, Mahmud!"),
#     ("human", "I'm learning LangChain."),
#     ("ai", "That's great, LangChain is a solid choice for building LLM apps."),
# ]

# final_prompt = template.format_messages(
#     chat_history=fake_history, question="What's my name?"
# )

# for msg in final_prompt:
#     print(f"{msg.type}: {msg.content}")

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os

# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
# )

# response = llm.invoke(final_prompt)
# print(response.content)


# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os

# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY"), temperature=0.7
# )

# template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are my senior software mentor."),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ]
# )
# fake_history = [
#     ("human", "My name is Mahmud."),
#     ("ai", "Nice to meet you, Mahmud!"),
#     ("human", "I'm learning LangChain."),
#     ("ai", "That's great, LangChain is a solid choice for building LLM apps."),
# ]

# final_prompt = template.format_messages(
#     chat_history = fake_history,
#     question = "What is my name?"
# )

# for msg in final_prompt:
#     print(f"{msg.type}: {msg.content}")

# response = llm.invoke(final_prompt)
# print(response.content[0]['text'])