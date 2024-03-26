
from dotenv import load_dotenv
import streamlit as st 
import os 
import google.generativeai as genai

load_dotenv(".env")

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    return response 


st.title("Chat with your own AI Assistant")

user_question = st.text_input("Ask a question")
button = st.button("Ask")

if button and user_question:
    result = LLM_Response(user_question)
    st.subheader("Response: ")
    for word in result:
        st.text(word.text)