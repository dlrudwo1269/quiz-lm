# run command: streamlit run Home.py
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title = "QuizLM",
    page_icon = "🎓"
)


st.markdown(
    """
    # Welcome to QuizLM! 🎓

    ---

    #### Hi! 👋 
    At **QuizLM**, we are dedicated to enhancing your learning experience through the power of artificial intelligence. Our platform is designed for **students**, **educators**, and **lifelong learners** alike, offering tools that transform text into powerful learning aids.

    ### Features
    - **FlashCard Generator**: Automatically creates flashcards from text input, helping users to quickly and efficiently generate study aids. This feature benefits users by breaking down complex information into manageable, question-and-answer pairs that facilitate better understanding and memorization.

    - **Quiz Generator**: Generates quizzes based on the provided text, offering an interactive way for users to test their knowledge and reinforce learning. This feature is useful for both self-assessment and instructional purposes, making the learning process more engaging and effective.

    Join us in revolutionizing the way we learn, one flashcard at a time!
    """,
    unsafe_allow_html=True
)