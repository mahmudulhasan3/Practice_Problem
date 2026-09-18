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





