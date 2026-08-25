# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# def get_required_env(key):
#     value = os.getenv(key)
#     if not value:
#         raise ValueError(f"Missing value: {key}")
#     return value

# api_key= get_required_env("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# model_name = get_required_env("GEMINI_MODEL_NAME")

# response = client.models.generate_content(
#     model=model_name,
#     config=genai.types.GenerateContentConfig(
#         system_instruction="You are a strict code reviewer, review code short and precise"
#     ),
#     contents="Look at this code:  for i in range(10):   print(i)"
# )
# print(response.text)

# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_required_key(key):
#     value = os.getenv(key)
#     if not value:
#         raise ValueError(f"Check .env file {key}")
#     return value

# api_key = get_required_key("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# model_name = get_required_key("GEMINI_MODEL_NAME")

# response = client.models.generate_content_stream(
#     model = model_name,
#     contents= "what is ai?"
# )

# for stream in response:
#     print(stream.text, end= "", flush= True)

# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()


# def get_required_key(key):
#     value = os.getenv(key)
#     if not value:
#         raise ValueError(f"Check .env file {key}")
#     return value


# api_key = get_required_key("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# model_name = get_required_key("GEMINI_MODEL_NAME")

# response = client.models.generate_content(
#     model=model_name,
#     contents="what is ai?",
#     config= {
#         "max_output_tokens" : 100
#     }
# )
# print(response.text)
# print(response.usage_metadata)

# model_info = client.models.get(model= model_name)
# print(model_info.output_token_limit)
# print(model_info.input_token_limit)

# from google import genai
# from dotenv import load_dotenv
# import os, time

# load_dotenv()


# def get_required_key(key):
#     value = os.getenv(key)
#     if not value:
#         raise ValueError(f"Check .env file {key}")
#     return value


# api_key = get_required_key("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# model_name = get_required_key("GEMINI_MODEL_NAME")

# for i in range(4):
#     response = client.models.generate_content(
#         model=model_name,
#         contents="give me one word to describe happy",
#         config={
#             "temperature": 1.5,
#             "top_p": 0.9,
#             "top_k": 3
#         }
#     )
#     time.sleep(1)
#     print(response.text)

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_required_key(key):
    value = os.getenv(key)
    if not value:
        raise ValueError(f"{key} is not found")
    return value

api_key = get_required_key("GEMINI_API_KEY")
client = genai.Client(api_key= api_key)

model_name = get_required_key("GEMINI_MODEL_NAME")

response = client.models.generate_content_stream(
    model=model_name, contents="Explain what a REST API is, in 3 sentences.",
    config={
        "temperature": 0.3,
        "max_output_tokens": 150,
        "top_p": 0.9
    }
)
for stream in response:
    print(stream.text, end= "", flush= True)
