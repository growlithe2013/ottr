import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def contactGemini(message):
    global client
    response=[]
    userMessages=[]
    user_prompt=sys.argv[1]
    userMessages.append(types.Content(role="user", parts=[types.Part(text=sys.argv[1])]))
    response.append(client.models.generate_content(model="gemini-2.0-flash-001", contents=userMessages))

    return response[-1]