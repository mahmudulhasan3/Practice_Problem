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


# import os
# from pydantic import BaseModel
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)


# class StudentInfo(BaseModel):
#     name: str
#     department: str
#     cgpa: float
#     skills: list[str]


# prompt = """
# আমার নাম Mahmud।
# আমি CSE department-এ পড়ি।
# আমার CGPA 3.85।
# আমি Python, FastAPI এবং LangChain জানি।
# """

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         response_mime_type="application/json", response_schema=StudentInfo
#     ),
# )
# student = response.parsed

# print(f"Name: {student.name}")
# print(f"Department: {student.department}")
# print(f"CGPA: {student.cgpa}")
# print(f"Skills: {student.skills}")


# main.py

# import os
# from dotenv import load_dotenv
# from google import genai
# from test import resume_analysis_prompt, classification_prompt, summarizer_prompt

# load_dotenv()
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# def ask_gemini(prompt: str) -> str:
#     """Generic function - যেকোনো prompt পাঠিয়ে answer আনে"""
#     response = client.models.generate_content(
#         model="gemini-3.5-flash-lite", contents=prompt
#     )
#     return response.text


# # --- ব্যবহার ---

# # 1. Resume analysis
# resume_text = "Built a Bangla RAG assistant using FastAPI and ChromaDB."
# prompt1 = resume_analysis_prompt(resume_text)
# print(ask_gemini(prompt1))

# # 2. Classification
# farmer_query = "আমার ধান গাছে পোকা লেগেছে, কী করব?"
# prompt2 = classification_prompt(
#     farmer_query, ["pest_control", "irrigation", "fertilizer", "other"]
# )
# print(ask_gemini(prompt2))

# # 3. Summarization with custom word limit
# long_text = "..."  # কোনো লম্বা article
# prompt3 = summarizer_prompt(long_text, max_words=30)
# print(ask_gemini(prompt3))


# import os
# import time
# from dotenv import load_dotenv
# from google import genai
# from google.genai import errors
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# def call_gemini_with_retry(prompt: str,max_retries: int = 3, wait: int = 2):
#     last_error = None
#     for attempt in range(1, max_retries + 1):
#         try:
#             response = client.models.generate_content(
#                 model="gemini-3.1-flash-lite",
#                 contents=prompt
#             )
#             return response.text

#         except errors.ClientError as e:
#             print(f"Non-retryable error (attempt {attempt}): {e}")
#             raise

#         except Exception as e:
#             last_error = e
#             print(f"Retryable error (attempt {attempt}/{max_retries}): {e}")

#             if attempt < max_retries:
#                 print(f"   Waiting {wait}s before retry...")
#                 time.sleep(wait)

#     raise RuntimeError(
#         f"All {max_retries} attempts failed. Last error: {last_error}"
#     )


# if __name__ == "__main__":
#     result = call_gemini_with_retry("Explain RAG in one line.")
#     print(result)


# import os
# import json
# from google import genai
# from dotenv import load_dotenv
# from google.genai import types

# def calculate_cost(input_tokens, output_tokens):
#     input_cost = (input_tokens/1000000) * 0.30
#     output_cost = (output_tokens/1000000) * 2.50
#     return input_cost + output_cost

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# response = client.models.generate_content(
#     model = "gemini-3.1-flash-lite",
#     contents= "What is ai?",

# )
# print(response.text)
# input_token = response.usage_metadata.prompt_token_count
# output_token = response.usage_metadata.candidates_token_count

# entry = {
#     "prompt": "What is ai?",
#     "input_token": input_token,
#     "output_token": output_token,
#     "total_cost": calculate_cost(input_token, output_token)
# }
# print(entry)
# with open("token_cost_calculation.jsonl", "a") as file:
#     file.write(json.dumps(entry) + "\n")

# Practice Task — Gemini Cost Tracker

# import os
# import json
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# def calculate_cost(input_cost,output_cost):
#     input_cost = (input_cost / 1000000) * 1
#     output_cost = (output_cost / 1000000) * 2
#     return input_cost + output_cost

# count = 0
# sum = 0
# input_token_sum = 0
# output_token_sum = 0
# while True:
#     prompt = input("Question: ")
#     if prompt.lower().strip() == "quit":
#         break
#     response = client.models.generate_content(
#         model = "gemini-3.1-flash-lite",
#         contents = prompt,
#     )
#     print(f"Answer: {response.text}")
#     input_token = response.usage_metadata.prompt_token_count
#     output_token = response.usage_metadata.candidates_token_count

#     input_token_sum += input_token
#     output_token_sum += output_token
#     count += 1
#     sum = input_token_sum + output_token_sum

#     print(f"Total Request: {count}")
#     print(f"Total input token: {input_token_sum}")
#     print(f"Total output token: {output_token_sum}")
#     print(f"Total token: {sum}")
#     print(f"Total cost: {calculate_cost(input_token_sum,output_token_sum)}")


# import os
# import json
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI-API-KEY")
# client = genai.Client(api_key= api_key)

# def calculate_cost(input_token, output_token):
#     input_cost = (input_token / 1000000) * 1
#     output_cost = (output_token / 1000000) * 2
#     return input_cost + output_cost

# total_token = 0
# count = 0
# input_token_total = 0
# output_token_total = 0
# while True:
#     prompt = input("\nQuestion: ")
#     if prompt.lower().strip() == "exit":
#         break
#     response = client.models.generate_content(
#         model = "gemini-3.1-flash-lite",
#         contents= prompt
#     )
#     print(response.text)
#     print(response.usage_metadata)
#     input_token = response.usage_metadata.prompt_token_count
#     output_token = response.usage_metadata.candidates_token_count

#     input_token_total += input_token
#     output_token_total += output_token

#     total_token = input_token_total + output_token_total
#     count += 1

#     print(f"Request: {count}")
#     print(f"Total token: {total_token}")
#     print(f"Total cost: {calculate_cost(input_token, output_token)}")


# CLI chatbot with conversation history

# import os
# import json
# from dotenv import load_dotenv
# from google import genai
# from google.genai import errors

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# history = []
# while True:
#     prompt = input("\nQuestion: ")
#     if prompt.lower().strip() == "exit":
#         with open("history.json", "w") as file:
#             file.write(json.dumps(history) + "\n")
#         break
#     if prompt == "":
#         raise TypeError("Please type a valid question")
#     history.append({"role": "user", "parts": [{"text": prompt}]})
#     try:
#         response = client.models.generate_content(
#             model="gemini-3.1-flash-lite", contents=history
#         )
#     except errors.ClientError as e:
#         print(e)
#         history.pop()
#         continue
#     except Exception as e:
#         print(e)
#         history.pop()
#         continue
#     history.append({"role": "model", "parts": [{"text": response.text}]})
#     print(response.text)


# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# while True:
#     prompt = input("\nQuestion: ")
#     if prompt.lower().strip() == "exit":
#         break
#     response = client.models.generate_content(
#         model="gemini-3.1-flash-lite",
#         contents=prompt
#     )
#     print(response.text)


# CLI chatbot with conversation history

# import os
# import json
# from dotenv import load_dotenv
# from google import genai
# from google.genai import errors

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# history = []
# while True:
#     prompt = input("\nQuestion: ")
#     if prompt.lower().strip() == "exit":
#         with open("history.json", "w") as file:
#             file.write(json.dumps(history) + "\n")
#         break
#     if prompt == "":
#         print("Enter valid input")
#         continue
#     history.append({"role": "user", "parts": [{"text": prompt}]})
#     try:
#         response = client.models.generate_content(
#             model="gemini-3.5-flash-lite", contents=history
#         )
#     except errors.ClientError as e:
#         print(e)
#         history.pop()
#         continue
#     except Exception as e:
#         print(e)
#         history.pop()
#         continue
#     history.append({"role": "model", "parts": [{"text": response.text}]})
#     print(response.text)


import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= api_key)

prompt_for_zero_shot = """
Classify the following text as positive or negative
Text: I really enjoy football
"""
prompt_for_few_shot = """
Classify the following text as positive or negative

Example-1:
Text: I enjoy football
Answer: positive

Example-2:
Text: I dont play cricket
Answer: Negative

Text: Cricket is a long time game and few peaple watch it, other people dont watch it

"""
response = client.models.generate_content(
    model = "gemini-3.1-flash-lite",
    contents = prompt_for_few_shot
)
print(response.text)