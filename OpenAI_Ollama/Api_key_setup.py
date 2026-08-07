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


# Streaming Advisory Bot with Usage Tracker

# import os
# import time
# import json
# from google import genai
# from dotenv import load_dotenv
# from datetime import datetime

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# model_name = os.getenv("GEMINI_MODEL")
# if not model_name:
#     raise TypeError("Error")

# total = 0
# while True:
#     persona = input("\nAssitant type: ")
#     if persona.lower().strip() == "exit":
#         break
#     prompt = input("\nQuestion: ")
#     response = client.models.generate_content_stream(
#         model=model_name, contents=prompt, config={"system_instruction": persona}
#     )
#     usage_metadata = None
#     for chunk in response:
#         if chunk.text:
#             for char in chunk.text:
#                 print(char, end="", flush=True)
#                 time.sleep(0.1)
#         if chunk.usage_metadata:
#             usage_metadata = chunk.usage_metadata
#     if usage_metadata:
#         input_token = usage_metadata.prompt_token_count
#         output_token = usage_metadata.candidates_token_count
#         total_token = usage_metadata.total_token_count
#         date_time = datetime.now().isoformat()
#         total += total_token

#         log = {
#             "input_token": input_token,
#             "output_token": output_token,
#             "total_token": total_token,
#             "datetime": date_time,
#         }
#         with open("prctice.jsonl", "a") as file:
#             file.write(json.dumps(log) + "\n")
# print(total)


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


# import os
# from google import genai
# from dotenv import load_dotenv
# from google.genai import types

# load_dotenv()
# api_keys = os.getenv("GEMINI_API_KEY")
# model_name = os.getenv("GEMINI_MODEL")
# client = genai.Client(api_key=api_keys)

# response = client.models.generate_content(
#     model = model_name,
#     contents = "Please suggest a name for my cat?",
#     config = types.GenerateContentConfig(
#         temperature=1.2,
#         top_k= 3,
#     ),
# )

# print(response.text)


# import os
# from google import genai
# from dotenv import load_dotenv
# from google.genai import types

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key= api_key)

# response = client.models.generate_content(
#     model = "gemini-3.1-flash-lite",
#     contents= "Suggest my child name",
#     config = types.GenerateContentConfig(
#         temperature= 0.3,
#         top_p = 0.9,
#         max_output_tokens= 500,
#         # frequency_penalty=0.5,
#         # presence_penalty= 0.3,
#     )
# )
# print(response.text)


# import os
# import json
# from google import genai
# from dotenv import load_dotenv
# from pydantic import BaseModel, Field
# from google.genai import types


# class Advice(BaseModel):
#     fertilizer_name: str = Field(description="সারের নাম")
#     dosage_grams: float = Field(description="পরিমাণ গ্রামে")
#     interval_days: int = Field(description="কত দিন পর পর")


# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)


# prompt = """
# আমার ধান ক্ষেতে ইউরিয়া সার ১৫ দিন পর পর ২০০ গ্রাম দিতে হবে।
# """
# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         response_mime_type="application/json", response_schema=Advice
#     ),
# )
# print(response.text)

# advice = response.parsed
# print(advice.fertilizer_name)
# print(advice.dosage_grams)
# print(advice.interval_days)



