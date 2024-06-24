# run command: streamlit run Home.py
import requests
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title = "QuizLM",
    page_icon = "🤖"
)

llm = ChatOllama(model="llama3")

def llama3(text):
    prompt = ChatPromptTemplate.from_template("Tell me a short joke about {text}")
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"text": text})

def process_input(text):
    text = f"""
    Create ten flashcards from the following text, enclosed in triple quotes:
    ```
    {text}
    ```
    """
    return llama3(text)

questions_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful assistant that is helping students to learn about a certain context.
            Based ONLY on the following context make 10 (TEN) questions to test the user's knowledge about the context.
            
         
    Use (o) to signal the correct answer.
         
    Question examples:
         
    Question: What is the color of the ocean?
    Answers: Red|Yellow|Green|Blue(o)
         
    Question: What is the capital or Georgia?
    Answers: Baku|Tbilisi(o)|Manila|Beirut
         
    Question: When was Avatar released?
    Answers: 2007|2001|2009(o)|1998
         
    Question: Who was Julius Caesar?
    Answers: A Roman Emperor(o)|Painter|Actor|Model
         
    Your turn!
         
    Context: {context}
""",
        )
    ]
)

with st.form(key='source_text'):
    user_input = st.text_area(label="Input text to create flashcards from")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    result = process_input(user_input)
    st.write("Result:", result)