import streamlit as st
import requests

def get_ollama_response(input_text):
    response = requests.post('http://localhost:8000/poem/invoke',
                             json={'input': {'topic':input_text}})
    return response.json()['output']


def get_openai_response(input_text):
    response = requests.post('http://localhost:8000/poem/invoke',
                             json={'input': {'topic':input_text}})
    return response.json()['output']['content']


st.title('Langchain Demo With OpenAI LLAMA2 API Chains')
input_text = st.text_input('Write a poem on')
input_text1 = st.text_input('Write an essay on')

if input_text:
    st.write(get_ollama_response(input_text))


if input_text1:
    st.write(get_openai_response(input_text1))
 