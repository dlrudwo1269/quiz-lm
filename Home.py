# run command: streamlit run Home.py
import streamlit as st

import requests

url = "http://localhost:11435/api/chat"

def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["message"]["content"]

st.set_page_config(
    page_title = "QuizLM",
    page_icon = "🤖"
)
def process_input(text):
    text = f"""Create ten flashcards from the following text, enclosed in triple quotes:
    ```
    {text}
    ```
    """
    return llama3(text)

with st.form(key='source_text'):
    user_input = st.text_area(label="Input text to create flashcards from")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    result = process_input(user_input)
    st.write("Result:", result)