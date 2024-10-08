LANGCHAIN_API_KEY = "xxxxxx"
OPENAI_API_KEY = ""
LANGCHAIN_PROJECT = "Chatbot_QA"
LANGCHAIN_TRACING_V2 = "true"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please provide response for my questions'),
        ('user','Question:{question}')
    ]
)

st.title('Langchain Demo With Open AI API')
input_text = st.text_input("search the topic you want")

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))


