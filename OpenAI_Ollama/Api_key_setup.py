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



import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    while True:
        choose = input("Choose a number 1/2/3/quit: ")
        if choose == "quit":
            break

        if choose == "1":
            while True:
                prompt = input("Question: ")
                if prompt == "quit":
                    break
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt,
                    config={"system_instruction": "তুমি একজন অভিজ্ঞ কৃষি বিশেষজ্ঞ..."},
                )
                print(response.text)

        elif choose == "2":
            while True:
                prompt = input("Question: ")
                if prompt == "quit":
                    break
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt,
                    config={"system_instruction": "তুমি একজন বন্ধুসুলভ কৃষক..."},
                )
                print(response.text)
        elif choose == "3":
            while True:
                prompt = input("Question: ")
                if prompt == "quit":
                    break
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt,
                    config={
                        "system_instruction": "তুমি শুধু ১-২ লাইনে সংক্ষিপ্ত উত্তর দাও..."
                    }
                )
                print(response.text)
        else:
            print("Wrong number choose, try again")

except Exception as e:
    print("Something is wrong", e)
