#
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from langserve import add_routes #through this we will be able to add all the routes to the FastAPI app
import uvicorn #to run the FastAPI app
import os #to get the environment variables
from dotenv import load_dotenv #to load the environment variables from the .env file
from langchain_ollama import OllamaLLM
 #to use Ollama as a language model

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") 

app=FastAPI(
    title="Langserve simple API Server",
    version="1.0",
    description="A simple API server using Langserve and FastAPI",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
          # Specify the model for Ollama
)

model=ChatOpenAI()


#ollama llama2
llm = OllamaLLM(model="llama2")


prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")
  

add_routes(

    app,
    prompt1|model,
    path="/essay"
)


add_routes(

    app,
    prompt2|llm,
    path="/poem"
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
# # This is a simple FastAPI server that uses Langserve to add routes for OpenAI and Ollama.
# # It uses the langchain library to create prompts and language models.
# # The server has two main routes: /essay and /poem.
# # The /essay route generates an essay based on the input topic using OpenAI.
# # The /poem route generates a poem based on the input topic using Ollama.
# # The server uses the dotenv library to load environment variables from a .env file.
# # The server is run using uvicorn, which is an ASGI server for FastAPI.
# # The server is designed to be run locally on port 8000.
# # The server uses the Langserve library to add routes to the FastAPI app.