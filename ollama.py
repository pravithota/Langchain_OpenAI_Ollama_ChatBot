LANGCHAIN_API_KEY = "xxxxxxx"
#OPENAI_API_KEY = ""
LANGCHAIN_PROJECT = "ChatbotQA"
LANGCHAIN_TRACING_V2 = "true"

#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


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

st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("search the topic you want")

llm = Ollama(model="llama2-uncensored")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question': input_text}))


