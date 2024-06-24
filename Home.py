# run command: streamlit run Home.py
import streamlit as st

st.set_page_config(
    page_title = "QuizLM",
    page_icon = "🤖"
)
def process_input(text):
    return text

with st.form(key='source_text'):
    user_input = st.text_area(label="Input text to create flashcards from")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    result = process_input(user_input)
    st.write("Result:", result)