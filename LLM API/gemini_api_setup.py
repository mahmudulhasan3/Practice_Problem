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

# response1 = client.models.generate_content(
#     model=model_name, 
#     contents="What is ai"
# )
# response2 = client.models.generate_content(
#     model = model_name,
#     contents= "Who is Andrew Ng?"
# )
# print(response1.text)
# print(response2.text)