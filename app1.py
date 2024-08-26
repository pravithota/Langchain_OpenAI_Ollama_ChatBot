from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
from langchain_community.llms import Ollama
#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

LANGCHAIN_API_KEY = "xxxxxxxxxxxxxx"
#OPENAI_API_KEY = ""
LANGCHAIN_PROJECT = "ChatbotQA"
LANGCHAIN_TRACING_V2 = "true"

app1 = FastAPI(
    title='Longchain Server',
    version='1.0',
    description='A Simple API Server'
)
'''
add_routes(
    app1,
    ChatOpenAI(),
    path='/openai'
)'''
# Open AI LLM Model
#model = ChatOpenAI()
# Open Ollma LLM Model
llm = Ollama(model='llama2-uncensored')

#prmopt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words")
prmopt2 = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5 years child")
'''
add_routes(
    app1,
    prmopt1|model,
    path='/essay' 
)'''

add_routes(
    app1,
    prmopt2|llm,
    path='/poem' 
)

if __name__=='__main__':
    uvicorn.run(app1, host='localhost', port=8000)


