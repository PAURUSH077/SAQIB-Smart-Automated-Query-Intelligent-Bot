import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])


def decide_action(command):
    prompt = f"""
    Decide whether the user wants:
    action OR chat

    Examples:
    "play music" → action
    "open youtube" → action
    "search phones" → action
    "what is python" → chat
    "tell me a joke" → chat

    Command: "{command}"

    Only return one word.
    """

    response = model.generate_content(prompt)
    return response.text.strip().lower()


def chat_with_ai(command):
    try:
        response = chat.send_message(command)
        return response.text.strip()
    except Exception as e:
        print("AI Error:", e)
        return "Sorry, something went wrong."