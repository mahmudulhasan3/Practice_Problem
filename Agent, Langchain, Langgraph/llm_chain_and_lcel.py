# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# import os

# load_dotenv()
# prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in simple terms for a beginner."
# )

# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite",
#     google_api_key=os.getenv("GEMINI_API_KEY"),
#     temperature=0.7,
# )
# parser = StrOutputParser()

# chain = prompt | llm | parser
# result = chain.stream({"topic": "vector database"})
# for chunk in result:
#     print(chunk, end= "", flush= True)


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "You are a {role}, answer this question: {question}"
)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
)

perser = StrOutputParser()

chain = prompt | llm | perser

response_invoke1 = chain.invoke(
    {"role": "a senior Python developer", "question": "What is a function?"}
)
response_invoke2 = chain.invoke(
    {"role": "a 10-year-old kid", "question": "What is a function?"}
)
response_stream = chain.stream(
    {"role": "a senior Python developer", "question": "What is a function?"}
)

for chunk in response_stream:
    print(chunk, end="", flush=True)

print(response_invoke1)
print(response_invoke2)
