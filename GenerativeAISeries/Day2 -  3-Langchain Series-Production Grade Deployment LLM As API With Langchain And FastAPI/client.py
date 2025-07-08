#Just imagine it as a web application client that interacts with a server.
import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic': input_text}})

    
    return response.json()['output']['content']


# Ollama # This function sends a request to the Ollama server to generate a poem based on the input text.
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic': input_text}})
    return response.json()['output']['content']


# Streamlit UI  
st.title("Langserve Client")
st.write("This is a simple client to interact with the Langserve API server.")
input_text = st.text_input("Enter a topic:")
if st.button("Generate Essay"):
    if input_text:
        essay = get_openai_response(input_text)
        st.write("Generated Essay:")
        st.write(essay)
    else:
        st.error("Please enter a topic.")
if st.button("Generate Poem"):
    if input_text:
        poem = get_ollama_response(input_text)
        st.write("Generated Poem:")
        st.write(poem)
    else:
        st.error("Please enter a topic.")
# This is a simple client to interact with the Langserve API server.
# It sends requests to the server and displays the responses in a Streamlit app.
# It uses the requests library to send HTTP requests to the server.
# The Streamlit library is used to create the user interface.
# The client has two main functions: get_openai_response and get_ollama_response.
# These functions send requests to the server to generate an essay and a poem, respectively.
# The responses are then displayed in the Streamlit app.
# The client also has a simple user interface with a text input for the topic and buttons to generate the essay and poem.
# The client is designed to be run in a Streamlit app, which provides an easy way to create web applications with Python.
# The client interacts with the Langserve API server to generate essays and poems based on user input.