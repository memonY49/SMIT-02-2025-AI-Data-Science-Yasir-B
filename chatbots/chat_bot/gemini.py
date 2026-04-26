from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()


client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


sys_msg = "You are a professional AI assistant for students from Sir Yasir's class. Only answer AI and Data Science questions. If asked about anything else, say you do not know."

response = client.models.generate_content(
    model='gemini-3-flash-preview', 
    contents="what is transformer?",
    config=types.GenerateContentConfig(
        system_instruction=sys_msg
    )
)
print(response.text)