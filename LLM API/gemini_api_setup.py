from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("API key is not found")
client = genai.Client(api_key= api_key)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite", 
    contents="What is ai"
)
print(response.text)