# 🤖 LangChain Chatbot Development Guide

This guide explains two primary ways to build AI-powered chatbots using [LangChain](https://www.langchain.com/) and [Streamlit](https://streamlit.io/). You can choose between:

- **Using Local LLMs** via [Ollama](https://ollama.com/) — for offline, private, and cost-free usage.
- **Using Cloud LLMs** via [OpenAI API](https://platform.openai.com/) — for high-performance and scalable chatbot deployments.

---

## 🧠 Overview: LangChain Chatbot Development

LangChain is a framework for building applications powered by language models. It allows us to use different LLMs (Large Language Models), combine them with custom prompts, and interact with them in a clean and chainable interface.

---

## ✅ Two Main Ways to Create Chatbots

### 1. Using Local LLMs (via Ollama)

- **Backend**: Uses models like `llama2` locally with the Ollama runtime.
- **No Internet Required** after initial setup.
- **Free & Private**: Data stays on your device.
- **Perfect for**: Offline demos, secure environments, R&D.

### 2. Using Cloud LLMs (via OpenAI API)

- **Backend**: Uses models like `gpt-3.5-turbo`, `gpt-4`.
- **Internet Required**.
- **Paid Service** (usage billed by OpenAI).
- **Perfect for**: Production-ready bots, SaaS, public tools.

---

## 🔧 Common Components in Both Methods

| Component                | Purpose                                                         |
|-------------------------|-----------------------------------------------------------------|
| `ChatPromptTemplate`     | Defines the format of the chatbot prompt (system & user roles)  |
| `StrOutputParser`        | Converts model response into plain strings                      |
| `Streamlit`              | Web framework to create interactive UI                          |
| `.env` file              | Securely stores API keys (e.g., `OPENAI_API_KEY`)               |
| `chain = prompt | llm | output_parser` | Constructs the full chatbot pipeline              |

---

## 🏗️ Step-by-Step Structure (for Both Methods)

### 1. Environment Setup

```python
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
