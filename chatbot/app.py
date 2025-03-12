from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question:{question}")
])

# Streamlit functions
st.title('Langchain demo with OpenAI')
input_text = st.text_input("Search the topic you want")

# OpenAI llm - simplified configuration
llm = ChatOpenAI(
    api_key=os.getenv("OPEN_API_KEY"),  # Changed to api_key
    model="gpt-3.5-turbo"
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))