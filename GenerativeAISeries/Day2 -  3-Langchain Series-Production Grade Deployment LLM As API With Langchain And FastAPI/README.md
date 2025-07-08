# Langserve API Server

## Overview

This repository contains a simple API server built using **FastAPI** and **Langserve**. The server integrates **OpenAI** and **Ollama** language models to generate essays and poems based on user input. It also includes a **Streamlit** client application for interacting with the server.

---

## Features

### Server
- **Essay Generation**: Generates essays using OpenAI's language model.
- **Poem Generation**: Generates poems using Ollama's language model.
- **Environment Variables**: Uses `dotenv` to load API keys securely.
- **Custom Routes**: Routes `/essay` and `/poem` are added using Langserve.

### Client
- **Streamlit UI**: A simple web interface for interacting with the API.
- **Dynamic Input**: Users can input topics to generate essays or poems.
- **HTTP Requests**: Sends requests to the server and displays responses.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd API
