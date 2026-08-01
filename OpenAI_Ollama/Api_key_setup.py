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


import os
from dotenv import load_dotenv
import google.genai as genai

try:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    while True:
        prompt = input("Question: ")

        if prompt == "quit":
            break
        response = client.models.generate_content(
            model= "gemini-flash-latest",
            contents= prompt
        )
        print(f"\nAnswer: {response.text}\n")

except Exception as e:
    print("Something is wrong", e)