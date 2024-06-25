import json
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from pages.prompts.flashcard_prompts import *
from langchain.chat_models import ChatOpenAI

models = ["gpt-3.5-turbo-1106", "gpt-4o", "llama3"]
# Disable Llama3 for production

# Page Setup
st.set_page_config(page_title = "FlashCard Generator", page_icon = "🗂️")
st.markdown("""# FlashCard Generator""", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Pasting Text Input", "Upload File"])

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

    api_key = st.text_input(
        "Enter your OpenAI API key:",
        placeholder="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        value= ""
    )


@st.cache_data(show_spinner="Making flashcards...")
def llama3(data, prompt_option):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system", PROMPT_OPTIONS[prompt_option],
            )
        ]
    )
    if model[:3] == 'gpt':
        llm = ChatOpenAI(
            temperature=0.1, 
            model_name="gpt-3.5-turbo-1106",
            streaming=True,
            api_key=api_key,
        )
    else:
        llm = ChatOllama(model="llama3")

    chain = prompt | llm
    return chain.invoke(data).content


def process_input(context, num_cards, prompt_option):
    data = {
        "context": context,
        "num_cards": num_cards
    }
    return llama3(data, prompt_option)


with tab1:
    with st.form(key='pasting_text'):
        user_input = st.text_area(
            label="Input text to create flashcards from:"
        )
        num_cards = st.number_input(
            label="How many cards do you want to generate?", min_value=1, max_value=999,
        )
        prompt_option = st.selectbox(
            "Select prompt option:",
            tuple(PROMPT_OPTIONS.keys()),
        )
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if user_input and len(user_input) > 30:
            result = process_input(context=user_input, num_cards=num_cards, prompt_option=prompt_option) 
            st.write("Result:", result.replace("$", "\$"))
        else:
            st.error("Please provide enough context to generate flashcards.")
        
with tab2:
    with st.form(key='file_text'):
        file = st.file_uploader(
                "Upload a .docx , .txt or .pdf file",
                type=["pdf", "txt", "docx"],
            )
        if file:
            pass
            # docs = split_file(file)
        
