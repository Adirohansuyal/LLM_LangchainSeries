#this app is all about how you can run local LLMs on your computer without the need for internet access, or depending on external and paid APIs.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "{question}")
    ]
)

# Streamlit app
st.title("Local LLM Chatbot with Ollama")
input_text = st.text_input("Search the topic you want")

# Ollama LLM model load, HERE'S THE KEY DIFFERENCE BETWEEN THIS AND THE API # VERSION, WE ARE USING OLLAMA TO LOAD A LOCAL LLM MODEL
llm = Ollama(model="llama2")  
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
# Note: Make sure you have Ollama installed and running with the model you want to use.
# You can run the Ollama server with the command: ollama serve
# Ensure you have the model downloaded, e.g., `ollama pull llama2`
# This app allows you to run a local LLM without needing internet access or relying on external APIs.