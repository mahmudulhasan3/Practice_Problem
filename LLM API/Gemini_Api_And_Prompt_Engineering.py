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
