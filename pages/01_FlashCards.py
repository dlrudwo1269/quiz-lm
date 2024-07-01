import os
import json
import socket
import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama

from pages.prompts.flashcard_prompts import *
from langchain.chat_models import ChatOpenAI


# Load env variables
load_dotenv()

models = ["gpt-3.5-turbo-1106", "gpt-4o"]

# DEV
try:
    environment = os.getenv('ENVIRONMENT')

# PROD
except:
    environment = "production"

if environment == "development":
    models.append("llama3")

# Page Setup
st.set_page_config(page_title = "FlashCard Generator", page_icon = "🗂️")
st.markdown("""# FlashCard Generator""", unsafe_allow_html = True)
tab1, tab2 = st.tabs(["Pasting Text Input", "Upload File"])

# CSS
current_dir = os.path.dirname(__file__)
css_file_flashcard = 'styles/01_FlashCards.css'
css_file_path = os.path.join(current_dir, css_file_flashcard)
with open(css_file_path, 'r') as file:
    card_css = "<style>" + file.read() + "</style>"
st.markdown(card_css, unsafe_allow_html=True)

PROMPT_OPTIONS = {
    "Zero-Shot": zeroshot_prompt,
    "Few-Shot": fewshot_prompt,
    "Chain-of-thought": chain_of_thought_prompt,
    "Analogy-Based": analogy_based_prompt,
}

with st.sidebar:
    model = st.sidebar.selectbox(
        "Which model would you like to use?",
        models,
        index = 0
    )

    if model[:3] == 'gpt':
        api_key = st.text_input(
            "Enter your OpenAI API key:",
            placeholder="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            value= "" if environment == "production" else os.getenv('OPENAI_API_KEY')
        )


@st.cache_data(show_spinner="Making flashcards...")
def generate(context, num_cards, prompt_option):

    # GPT Models
    if model[:3] == 'gpt':
        from langchain.prompts import ChatPromptTemplate
        from langchain.schema import BaseOutputParser

        llm = ChatOpenAI(temperature=0.5, model_name=model, streaming=True, api_key=api_key)
        flashcard_prompt = ChatPromptTemplate.from_messages([("system", PROMPT_OPTIONS[prompt_option],)])
        formatting_prompt = ChatPromptTemplate.from_messages([("system", json_output_prompt,)])
        flashcard_chain = flashcard_prompt | llm
        formatting_chain = formatting_prompt | llm
        
        class JsonOutputParser(BaseOutputParser):
            def parse(self, text):
                text = text.replace("```", "").replace("json", "")
                return json.loads(text)

        chain = {"questions": flashcard_chain} | formatting_chain | JsonOutputParser()
        return chain.invoke({"context": context, "num_cards": num_cards})
    
    # Ollama Model
    else:
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        llm = ChatOllama(model="llama3")
        prompt = ChatPromptTemplate.from_template(PROMPT_OPTIONS[prompt_option])
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"context": context, "num_cards": num_cards})
    
with tab1:
    with st.form(key='pasting_text'):
        user_input = st.text_area(
            label="Input text to create flashcards from:"
        )
        num_cards = st.number_input(
            label="How many cards do you want to generate?", min_value=1, max_value=100,
        )
        prompt_option = st.selectbox(
            "Select prompt option:",
            tuple(PROMPT_OPTIONS.keys()),
        )
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if user_input and len(user_input) > 30:
            result = generate(context=user_input, num_cards=num_cards, prompt_option=prompt_option)
            
            if model[:3] == 'gpt':
                for q in result["questions"]:
                    question, answer = q["question"], q["answer"]
                    st.write("Question:", question)
                    st.write("Answer:", answer)
                    st.write("---")
            else:
                st.write(result)
            
        else:
            st.error("Please provide enough context to generate flashcards.")
        
with tab2:
    with st.form(key='file_text'):
        file = st.file_uploader(
                "Upload a .docx , .txt or .pdf file",
                type=["pdf", "txt", "docx"],
            )
        num_cards = st.number_input(
            label="How many cards do you want to generate?", min_value=1, max_value=100,
        )
        prompt_option = st.selectbox(
            "Select prompt option:",
            tuple(PROMPT_OPTIONS.keys()),
        )
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if file:
                pass
                # docs = split_file(file)
        
