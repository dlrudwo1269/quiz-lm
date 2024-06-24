# run command: streamlit run Home.py
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pages.prompts.flashcard_prompts import *

PROMPT_OPTIONS = {
    "Zero-shot": zeroshot_prompt,
    "Few-shot": fewshot_prompt,
    "Chain of thought": chain_of_thought_prompt,
    "Summarize then Generate": "text4"
}

llm = ChatOllama(model="llama3")

st.set_page_config(
    page_title = "QuizLM",
    page_icon = "🤖"
)

def llama3(data, prompt_option):
    prompt = ChatPromptTemplate.from_template(PROMPT_OPTIONS[prompt_option])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke(data)


def process_input(context, num_cards, prompt_option):
    data = {
        "context": context,
        "num_cards": num_cards
    }
    return llama3(data, prompt_option)


with st.form(key='source_text'):
    user_input = st.text_area(label="Input text to create flashcards from")
    num_cards = st.number_input(
        label="How many cards do you want to generate?", min_value=0, max_value=999,
    )
    prompt_option = st.selectbox(
         "Select prompt option:",
        tuple(PROMPT_OPTIONS.keys()),
    )
    submit_button = st.form_submit_button(label='Submit')


if submit_button:
    result = process_input(context=user_input, num_cards=num_cards, prompt_option=prompt_option) 
    st.write("Result:", result)
