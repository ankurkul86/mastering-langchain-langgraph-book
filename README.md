# Mastering LangChain and LangGraph

[![Official Website](https://img.shields.io/badge/Official%20Website-masteringlangchainlanggraph.com-0052CC?style=for-the-badge&logo=google-chrome&logoColor=white)](https://masteringlangchainlanggraph.com/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain 1.3.10](https://img.shields.io/badge/LangChain-1.3.10-1C3C3C.svg?style=for-the-badge)](https://www.langchain.com/)
[![LangGraph 1.2.6](https://img.shields.io/badge/LangGraph-1.2.6-FF6F00.svg?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)

> **Official companion code repository for the book *Mastering LangChain and LangGraph* by Ankur Kulshreshtha (published by Springer Apress).**

> [!NOTE]
> **Tested & Verified Environment:** All code in this repository has been tested and verified against **`langchain==1.3.10`** and **`langgraph==1.2.6`**.

For book overview, table of contents, and updates, visit the official website:  
👉 **[https://masteringlangchainlanggraph.com/](https://masteringlangchainlanggraph.com/)**

---

## 📖 About The Book

*Mastering LangChain and LangGraph* is a comprehensive, hands-on guide designed for AI engineers, data scientists, and system architects building enterprise-grade **Retrieval-Augmented Generation (RAG)** systems and **Agentic AI** workflows.

From fundamental LLM integrations and prompt engineering to complex multi-agent architectures, cyclic graph workflows, Model Context Protocol (MCP) integrations, human-in-the-loop state machines, and streaming pipelines, this repository provides production-ready code examples covering the latest **LangChain v1.0** and **LangGraph v1.0** ecosystems.

---

## 🚀 Getting Started

Follow the steps below to set up your local development environment.

### 1. Prerequisites

- **Python 3.10+** (Python 3.11 recommended)
- **Git**
- Recommended editor: [VS Code](https://code.visualstudio.com/) with Jupyter extension or [JupyterLab](https://jupyter.org/)

---

### 2. Clone the Repository

```bash
git clone https://github.com/ankurkul86/mastering-langchain-langgraph-book.git
cd mastering-langchain-langgraph-book
```

---

### 3. Create and Activate a Virtual Environment (`.venv`)

It is strongly recommended to isolate dependencies inside a virtual environment:

#### On macOS / Linux:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### On Windows (Command Prompt / PowerShell):
```cmd
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Command Prompt)
.venv\Scripts\activate.bat

# Or in PowerShell:
.venv\Scripts\Activate.ps1
```

---

### 4. Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables (`.env`)

Many notebooks require API credentials from model providers (OpenAI, Anthropic, Google Gemini, Groq, Mistral) and search services (Tavily).

1. Copy the sample environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and fill in your personal API keys:

```env
# ==========================================
# LLM Provider Keys
# ==========================================
OPENAI_API_KEY="your-openai-api-key-here"
ANTHROPIC_API_KEY="your-anthropic-api-key-here"
GEMINI_API_KEY="your-gemini-api-key-here"
MISTRAL_API_KEY="your-mistral-api-key-here"
GROQ_API_KEY="your-groq-api-key-here"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token-here"

# ==========================================
# Search & External Tools
# ==========================================
TAVILY_API_KEY="your-tavily-api-key-here"
```

> ⚠️ **Security Notice:** Never commit your `.env` file to version control. The included [.gitignore](.gitignore) ensures `.env` is ignored by Git.

---

### 6. Launch Jupyter

Run JupyterLab or Jupyter Notebook inside the activated environment:

```bash
jupyter lab
# or
jupyter notebook
```

---

## 📂 Repository Structure & Chapter Mapping

| Chapter Notebook / File | Title & Description |
| :--- | :--- |
| **Part 2: Integrations & Utilities For LLM In LangChain** | |
| [`Chap-03 Chat Models.ipynb`](./Chap-03%20Chat%20Models.ipynb) | **Chat Models:** Interfacing with OpenAI, Anthropic, Gemini, Groq, Mistral, and local Ollama models. |
| [`Chap-04 Generating Structured Outputs.ipynb`](./Chap-04%20Generating%20Structured%20Outputs.ipynb) | **Structured Outputs:** Typed schemas, Pydantic validation, instructor-style extraction, and function calling. |
| [`Chap-05 Prompt Templates.ipynb`](./Chap-05%20Prompt%20Templates.ipynb) | **Prompt Templates:** Dynamic prompt building, few-shot prompt templates, chat message composition. |
| **Part 3: Integrations & Utilities For RAG In LangChain** | |
| [`Chap-06 Document Loader.ipynb`](./Chap-06%20Document%20Loader.ipynb) | **Document Loaders:** Ingesting PDFs, CSV, HTML, Markdown, Docling, and web sources. |
| [`Chap-07 Text Splitters.ipynb`](./Chap-07%20Text%20Splitters.ipynb) | **Text Splitters:** Character, Recursive Character, Token-based, Markdown, and Semantic chunking. |
| [`Chap-08 Embeddings & Vector Stores.ipynb`](./Chap-08%20Embeddings%20%26%20Vector%20Stores.ipynb) | **Embeddings & Vector Stores:** Dense embeddings, ChromaDB, vector indexing, similarity search. |
| [`Chap-09 Retrievers.ipynb`](./Chap-09%20Retrievers.ipynb) | **Retrievers:** Multi-query retrievers, contextual compression, parent document retrievers, ensemble search. |
| **Part 4: Build Agents With LangGraph** | |
| [`Chap-10 Fundamentals of LangGraph.ipynb`](./Chap-10%20Fundamentals%20of%20LangGraph.ipynb) | **Fundamentals of LangGraph:** State graphs, nodes, conditional edges, cyclic control flows, routing. |
| [`Chap-11 Tools & Model Context Protocol (MCP).ipynb`](./Chap-11%20Tools%20%26%20Model%20Context%20Protocol%20(MCP).ipynb) | **Tools & MCP:** Custom tools, tool calling, and integrating Model Context Protocol (MCP) servers. |
| ├── [`news_mcp_server.py`](./news_mcp_server.py) | *FastMCP news server providing real-time simulated market & company news feeds.* |
| └── [`stock_market_mcp_server.py`](./stock_market_mcp_server.py) | *FastMCP financial server providing live stock prices and buy/sell execution.* |
| [`Chap-12 Checkpointers.ipynb`](./Chap-12%20Checkpointers.ipynb) | **Checkpointers:** State persistence, SQLite checkpointing, thread isolation, session recovery. |
| [`Chap-13 Implementing Memory.ipynb`](./Chap-13%20Implementing%20Memory.ipynb) | **Implementing Memory:** Short-term conversational buffer memory and persistent long-term memory stores. |
| [`Chap-14 Human-In-The-Loop, Time Travel & Streaming.ipynb`](./Chap-14%20Human-In-The-Loop,%20Time%20Travel%20%26%20Streaming.ipynb) | **HITL & Streaming:** Human verification interrupts, state editing, time travel replay, and token streaming. |
| **Part 5: LangChain Agents** | |
| [`Chap-15 Fundamentals Of LangChain Agents.ipynb`](./Chap-15%20Fundamentals%20Of%20LangChain%20Agents.ipynb) | **LangChain Agents:** ReAct agent design, tool binding, loop execution, and agent runtimes. |
| [`Chap-16 Middlewares.ipynb`](./Chap-16%20Middlewares.ipynb) | **Middlewares:** Interceptors, hooks, observability wrappers, error fallback handlers, and guardrails. |
| **Appendix** | |
| [`Chap-17 Runnables & LCEL.ipynb`](./Chap-17%20Runnables%20%26%20LCEL.ipynb) | **Runnables & LCEL:** LangChain Expression Language, pipes (`\|`), batching, fallback chains, parallelism. |
| [`Chap-18 Python Typing & Pydantic.ipynb`](./Chap-18%20Python%20Typing%20%26%20Pydantic.ipynb) | **Python Typing & Pydantic:** Modern Python type annotations, Pydantic v2 schemas, model validation. |

---

## 🛠️ Model Context Protocol (MCP) Servers

Chapter 11 demonstrates connecting LangGraph agents to standardized **Model Context Protocol (MCP)** tools. You can run the included standalone FastMCP servers in separate terminals:

```bash
# Terminal 1: Run the news MCP server
python news_mcp_server.py

# Terminal 2: Run the stock market trading MCP server
python stock_market_mcp_server.py
```

These servers expose streaming HTTP endpoints that your LangGraph agents can query dynamically for real-time information and external actions.

---

## 📂 Sample Documents

The [`documents/`](./documents/) folder provides sample data files (PDFs, CSVs, TXT, HTML) used in **Chapter 6 (Document Loaders)**, **Chapter 7 (Text Splitters)**, and **Chapter 8 & 9 (RAG & Retrieval)**.

---

## ✍️ About the Author

**Ankur Kulshreshtha** is an AI practitioner, author, and engineer specializing in Large Language Models, agentic architectures, and enterprise AI workflows.

- 🌐 **Book Website:** [https://masteringlangchainlanggraph.com/](https://masteringlangchainlanggraph.com/)
- 👤 **Personal Website:** [https://ankurkulshreshtha.com/](https://ankurkulshreshtha.com/)
- ✍️ **Blog:** [Machine Learning Knowledge](https://machinelearningknowledge.com/)
- 📚 **Publisher:** Springer Apress

---

## 📄 License & Usage

The code in this repository is provided to accompany the book *Mastering LangChain and LangGraph*. You are free to use, modify, and integrate these examples in your own learning and projects.
