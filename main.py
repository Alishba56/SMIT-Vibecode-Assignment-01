import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are EduBot, an Education Chatbot.

You help students with:
- Mathematics
- Science
- Computer Science
- Programming
- English
- Homework
- Study techniques
- General educational questions

Rules:
1. Greet the user politely.
2. Give specific and relevant answers.
3. Explain difficult topics step by step.
4. Remember the conversation and answer follow-up questions using context.
5. Do not answer unrelated questions.
6. Do not help with hacking, weapons, violence, illegal activities, or harmful requests.
7. If a request is outside education, politely say:
   "Sorry, I can only help with educational topics."
8. Keep answers simple and easy to understand.
9. When the user says goodbye, end the conversation politely.
"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

print("===================================")
print("          Welcome to EduBot")
print("       Your Education Chatbot")
print("===================================")

print("EduBot: Hello! I am EduBot.")
print("EduBot: I can help you with educational questions.")
print("EduBot: Type 'exit' or 'bye' to end the conversation.\n")


while True:

    user_input = input("You: ")

    if user_input.lower().strip() in ["exit", "quit", "bye", "goodbye"]:
        print("EduBot: Goodbye! Keep learning and have a great day!")
        break

    if user_input.strip() == "":
        print("EduBot: Please enter a question.")
        continue

    try:
        response = chat.send_message(user_input)

        print("EduBot:", response.text)

    except Exception as e:
        print("EduBot: Sorry, something went wrong.")
        print("Error:", e)