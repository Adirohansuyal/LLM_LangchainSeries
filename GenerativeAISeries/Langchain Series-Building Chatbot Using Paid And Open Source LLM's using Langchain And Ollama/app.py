
#This script creates a chatbot using LangChain and OpenAI, with Streamlit providing the user interface. It loads environment variables, sets up a prompt template, initializes the OpenAI model, and processes user input to generate responses.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#The above three will be definitliy needed

import streamlit as st
import os
from dotenv import load_dotenv


#STEP 2 OF LOADING ENVIRONMENT VARIABLES {LANGSMITH TRACKING}
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

3 #PROMPT TEMPLATE

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user's queries"),
        ("user", "{Question:{question}")
    ]
)


#STREAMLIT APP

st.title("LangChain OpenAI Chatbot")
input_text = st.text("Search the topic you want")

# OPENAI LLM MODEL LOAD

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))