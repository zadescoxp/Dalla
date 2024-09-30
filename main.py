import google.generativeai as genai
import speech

genai.configure(api_key="AIzaSyDsTRGDDe-5LIO0j_4RjlklOUEyxZCxGXQ")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat(history=[])
while True:
    question = speech.listen()
    response = chat.send_message(question, stream=False)
    print("Bot " + response.text)
