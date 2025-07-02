# Financial Data Retrieval and Summarization

## Case Study: Financial Data Retrieval and Summarization

### Problem Statement
Investors and analysts often need quick access to accurate and summarized financial data, such as stock prices, analyst recommendations, company fundamentals, and news. Manually searching for this information across multiple platforms is time-consuming and error-prone. The challenge is to create an automated system that retrieves, processes, and presents this data in a user-friendly format.

---

### Solution
The `financial_agent.py` script implements a multi-agent system to address this problem. It combines the capabilities of two specialized agents: a **Web Search Agent** and a **Financial Agent**, orchestrated by a **Multi-Agent Team**. The system uses AI models and tools to automate the retrieval and summarization of financial information.

---

### Key Components

#### Web Search Agent:
- **Purpose**: Searches the web for financial information.
- **Technology**: Uses the `DuckDuckGo` tool for web searches.
- **AI Model**: Powered by the `Groq` AI model (`llama3-groq-70b-8192-tool-use-preview`).
- **Features**:
  - Includes sources in the output.
  - Outputs results in markdown format.
  - Displays tool calls for transparency.

#### Financial Agent:
- **Purpose**: Retrieves financial data from Yahoo Finance.
- **Technology**: Uses the `YFinanceTools` tool for:
  - Stock prices
  - Analyst recommendations
  - Stock fundamentals
  - Company news
- **AI Model**: Also powered by the `Groq` AI model.
- **Features**:
  - Displays data in tables.
  - Outputs results in markdown format.
  - Shows tool calls for transparency.

#### Multi-Agent Team:
- **Purpose**: Combines the capabilities of the Web Search Agent and Financial Agent.
- **Functionality**:
  - Processes complex queries like "Summarize analyst recommendation and share the latest news for NVIDIA."
  - Ensures outputs are well-structured with sources and tables.

---

### Workflow
1. **Input**: A query is provided to the `multi_ai_agent`, such as "Summarize analyst recommendation and share the latest news for NVIDIA."
2. **Processing**:
   - The Web Search Agent retrieves relevant web-based information.
   - The Financial Agent fetches structured financial data from Yahoo Finance.
3. **Output**:
   - The results are combined and presented in markdown format.
   - Data is displayed in tables, and sources are included for credibility.

---

### Tech Stack
- **Programming Language**: Python
- **AI Model**: `Groq` (`llama3-groq-70b-8192-tool-use-preview`)
- **Tools**:
  - `DuckDuckGo`: For web searches.
  - `YFinanceTools`: For financial data retrieval.
- **Libraries**:
  - `phidata`: Provides the `Agent` class and tool integrations.

---

### Benefits
- **Automation**: Eliminates the need for manual data collection.
- **Accuracy**: Ensures reliable data by including sources.
- **Efficiency**: Processes queries quickly and presents results in a structured format.
- **Transparency**: Displays tool calls for better understanding of the process.

---

### Use Case Example
- **Scenario**: A financial analyst wants to evaluate NVIDIA's stock performance and recent news.
- **Query**: "Summarize analyst recommendation and share the latest news for NVIDIA."
- **Output**:
  - A table summarizing analyst recommendations.
  - A list of recent news articles with sources.
  - Stock price and fundamental data.

---

### Notes
- **Environment Variables**: The `.env` file is ignored in version control as specified in the `.gitignore` file. Ensure to configure your API keys and sensitive data in the `.env` file.

This system demonstrates how AI-powered agents can streamline financial data retrieval and analysis, making it a valuable tool for investors, analysts, and researchers.