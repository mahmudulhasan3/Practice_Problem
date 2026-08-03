# import os
# from dotenv import load_dotenv
# import google.genai as genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# response =client.models.generate_content (
#     model = "gemini-flash-latest",
#     contents = "Who i am?"
# )

# print(response.text)


# import os
# from dotenv import load_dotenv
# import google.genai as genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents=input("Enter what you want: ")
# )
# print(response.text)


# import os
# from dotenv import load_dotenv
# import google.genai as genai

# try:
#     load_dotenv()
#     api_key = os.getenv("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)

#     response = client.models.generate_content(
#         model= "gemini-flash-latest",
#         contents= "what is niter,nayarhat, dhaka"
#     )

#     print(response.text)

# except Exception as e:
#     print("Something is wrong", e)


# import os
# from dotenv import load_dotenv
# from google import genai

# try:
#     load_dotenv()
#     api_key = os.getenv("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)

#     while True:
#         prompt = input("Question: ")

#         if prompt == "quit":
#             break
#         response = client.models.generate_content(
#             model="gemini-3.5-flash-lite", contents=prompt
#         )
#         print(f"\nAnswer: {response.text}\n")

# except Exception as e:
#     print("Something is wrong", e)

# import os
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# try:
#     while True:
#         prompt = input("Question: ")
#         if prompt == "quit":
#             break
#         response = client.models.generate_content(
#             model="gemini-3.5-flash-lite",
#             contents=prompt,
#             config={
#                 "system_instruction": "আমি তোমাকে যেই প্রশ্নই করি না কেন, তুমি শুধু বলবা, I love niter"
#             }
#         )
#         print(f"\nAnswer: {response.text}\n")
# except Exception as e:
#     print(f"Something is wrong, {e}")


# import os
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# try:
#     while True:
#         choose = input("Choose a number 1/2/3/quit: ")
#         if choose == "quit":
#             break

#         if choose == "1":
#             while True:
#                 prompt = input("Question: ")
#                 if prompt == "quit":
#                     break
#                 response = client.models.generate_content(
#                     model="gemini-3.5-flash-lite",
#                     contents=prompt,
#                     config={"system_instruction": "তুমি একজন অভিজ্ঞ কৃষি বিশেষজ্ঞ..."},
#                 )
#                 print(response.text)

#         elif choose == "2":
#             while True:
#                 prompt = input("Question: ")
#                 if prompt == "quit":
#                     break
#                 response = client.models.generate_content(
#                     model="gemini-3.5-flash-lite",
#                     contents=prompt,
#                     config={"system_instruction": "তুমি একজন বন্ধুসুলভ কৃষক..."},
#                 )
#                 print(response.text)
#         elif choose == "3":
#             while True:
#                 prompt = input("Question: ")
#                 if prompt == "quit":
#                     break
#                 response = client.models.generate_content(
#                     model="gemini-3.5-flash-lite",
#                     contents=prompt,
#                     config={
#                         "system_instruction": "তুমি শুধু ১-২ লাইনে সংক্ষিপ্ত উত্তর দাও..."
#                     }
#                 )
#                 print(response.text)
#         else:
#             print("Wrong number choose, try again")

# except Exception as e:
#     print("Something is wrong", e)


# import os
# import time
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# stream = client.models.generate_content_stream(
#     model="gemini-3.1-flash-lite",
#     contents="What is AI?",
# )
# for chunk in stream:
#     if chunk.text:
#         for char in chunk.text:
#             print(char, end="", flush=True)
#             time.sleep(0.1)
# print()

# import os, time
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# model_name = os.getenv("GEMINI_MODEL")
# if model_name is None:
#     raise ValueError("GEMINI_MODEL not find in .env file")
# try:
#     while True:
#         prompt = input("\n\nQuestion: ")
#         if prompt == "quit":
#             break
#         stream = client.models.generate_content_stream(
#             model=model_name,
#             contents=prompt,
#             config={"system_instruction": "Answer in 3 line always"},
#         )
#         print("\nAnswer: ")
#         for chunk in stream:
#             if chunk.text:
#                 for char in chunk.text:
#                     print(char, end="", flush=True)
#                     time.sleep(0.1)
# except Exception as e:
#     print("Something is wrong", e)


# import os
# from google import genai
# from dotenv import load_dotenv
# from google.genai import types

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# model_name = os.getenv("GEMINI_MODEL")

# def call_with_logging(system_instruction: str, user_message: str):
#     stream = client.models.generate_content_stream(
#         model= model_name,
#         contents= [{
#             "role": "user",
#             "parts": [{"text": user_message}]
#         }]
#         config=types.GenerateContentConfig(
#             "system_instruction": system_instruction
#     )
#     usage = stream.use

# from google import genai
# from dotenv import load_dotenv
# import os
# import json

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# model_name = os.getenv("GEMINI_MODEL")

# response = client.models.generate_content(
#     model=model_name, 
#     contents="Explain FastAPI in simple language."
# )
# log = {
#     "prompt_token": response.usage_metadata.prompt_token_count,
#     "candidate_token": response.usage_metadata.candidates_token_count,
#     "total_token": response.usage_metadata.total_token_count
# }

# with open("logger.jsonl", "a") as file:
#     file.write(json.dumps(log) + "\n")


