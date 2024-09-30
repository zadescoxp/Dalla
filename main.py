import google.generativeai as genai
import speech
import os

genai.configure(api_key=os.environ.get("GEMINI_API"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat(history=[])
while True:
    question = speech.listen()
    response = chat.send_message(question, stream=False)
    print("Bot " + response.text)
