import streamlit as st
from langchain_community.chat_models import ChatOllama

# Page Design
st.set_page_config(
    page_title="Flash Cards",
    page_icon="",
)

st.markdown(
    """
# FlashCards
        
Welcome to FlashCards.

FlashCards assists you ...

<span style="color:red; font-weight:bold;">[Disclaimer] The results provided by this agent are for informational purposes only and may be incorrect. </span>
""",
    unsafe_allow_html=True
)


with st.sidebar:
    prompt_method = st.sidebar.selectbox(
        "Which type of prompt would you like to use?",
        ["Zero-Shot", "Few-Shot", "Chain-of-Thought", "Iterative Refinement", "Analogy-Based"]
    )