# servicios/gemini.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

def geminiGenerador(prompt: str):
    response = model.generate_content(prompt)
    return response.text
