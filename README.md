<div align="center">

# 🧠 Multi-PDF Chatbot (RAG-based)
### *Chat with Any PDF Document — Privately, Locally, Intelligently*

<br/>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-0066CC?style=for-the-badge)](https://faiss.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

> **"Upload PDFs. Ask anything. Get accurate, context-aware answers — 100% offline."**

</div>

---

## 🎯 What is Multi-PDF Chatbot?

**Multi-PDF Chatbot** is a production-grade intelligent document assistant built on **Retrieval-Augmented Generation (RAG)** architecture. It enables natural language conversations across multiple PDF documents simultaneously — all running **locally on your machine** with zero cloud dependency, zero data leakage.

Whether you're analyzing research papers, legal contracts, financial reports, or technical manuals — this system extracts knowledge and answers your questions with precision using state-of-the-art local LLMs.

<br/>

---

## 🖥️ Live Demo

### 📌 Application Interface
The full-stack chatbot UI built with Streamlit — sleek, dark-themed, and intuitive.

![Application Screenshot](img/LLMframework.png)

> *Upload multiple PDF files via the sidebar → Ask your question in natural language → Receive detailed, evidence-based answers from your local LLM.*

<br/>

### 🔬 Real-World Test: CALM Paper Analysis
Uploaded and queried the **"Compositionality by Abstraction (CALM)"** research paper from arXiv. The model accurately synthesized the paper's core contribution — the CALM framework for composing anchor and augmenting LLMs.

![CALM Paper Output](img/CALMOutput.png)

> *Asked: "talk about this book's purpose in detail" — RAG retrieved the most relevant chunks and the LLM delivered a structured, accurate response about the CALM framework.*

<br/>

---

## 🏗️ System Architecture

The diagram below illustrates the complete **RAG pipeline** — from raw PDF input to final AI-generated answer.

![Project Flow Architecture](img/Architecture.jpg)

### ⚙️ How it Works — Step by Step

| Step | Stage | Description |
|------|-------|-------------|
| **1** | 📄 **Document Ingestion** | User uploads one or more PDF files via the Streamlit sidebar |
| **2** | ✂️ **Text Chunking** | Documents are split into overlapping chunks (5,000 chars / 1,000 overlap) using `RecursiveCharacterTextSplitter` |
| **3** | 🔢 **Embedding Generation** | Each chunk is converted into a high-dimensional vector using `qwen3-embedding` via Ollama |
| **4** | 🗄️ **Vector Store (FAISS)** | Embeddings are indexed locally in a FAISS vector database for millisecond-speed semantic retrieval |
| **5** | ❓ **Query Processing** | User's question is embedded using the same model to preserve semantic consistency |
| **6** | 🔍 **Semantic Search** | FAISS performs similarity search and retrieves the top-k most relevant chunks |
| **7** | 🤖 **LLM Generation** | Retrieved context + question is fed to `llama3.1:8b` via Ollama for final answer synthesis |

<br/>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Role |
|-------|-----------|------|
| **Frontend** | Streamlit | Interactive web UI with dark mode |
| **Orchestration** | LangChain | Pipeline management, prompting, QA chain |
| **LLM Inference** | Ollama + `llama3.1:8b` | Local, private language model serving |
| **Embeddings** | Ollama + `qwen3-embedding` | Semantic vector representations |
| **Vector Search** | FAISS | Ultra-fast local similarity retrieval |
| **PDF Parsing** | PyPDF2 | Multi-page text extraction |

</div>

<br/>

---

## ✨ Key Features

- 🔒 **100% Private & Local** — No API keys, no cloud, no data leaving your machine
- 📚 **Multi-Document Intelligence** — Query across many PDFs in one unified knowledge base
- 🧩 **Overlap-Aware Chunking** — Sliding window strategy prevents context loss at chunk boundaries
- ⚡ **FAISS Acceleration** — Sub-millisecond semantic vector search at scale
- 🔄 **Plug-and-Play LLMs** — Swap any Ollama-compatible model with a one-line config change
- 🎨 **Clean Streamlit UI** — Real-time processing feedback, spinner state management, intuitive layout

<br/>

---

## 🚀 Getting Started

### Prerequisites

```
Python 3.9+
Ollama (Desktop or Server runtime)
```

<br/>

### 1️⃣ Clone & Set Up Environment

```bash
git clone https://github.com/your-username/MultiPDF_RAG.git
cd MultiPDF_RAG

# Create and activate virtual environment
python3 -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 3️⃣ Pull Local LLM Models via Ollama

```bash
# Install Ollama from https://ollama.com then:
ollama pull llama3.1:8b        # Chat / reasoning model
ollama pull qwen3-embedding    # Embedding model
```

### 4️⃣ Launch the Application

```bash
python3 -m streamlit run chatapp.py
```

The app opens automatically at `http://localhost:8501` 🎉

<br/>

---

## 📖 Usage Guide

```
1. Launch the app with the command above
2. In the LEFT SIDEBAR — upload one or more PDF files
3. Click [Submit & Process] and wait for the ✅ Done confirmation
4. In the MAIN PANEL — type any natural language question
5. Read the AI-generated, context-grounded answer
```

> 💡 **Pro Tip**: Ask specific, targeted questions for best results. The RAG system retrieves the most semantically relevant passages before generating an answer.

<br/>

---

## 📁 Project Structure

```
MultiPDF_RAG/
├── chatapp.py          # Main Streamlit application entry point
├── requirements.txt    # Python dependency manifest
├── img/
│   ├── Architecture.jpg    # RAG pipeline flow diagram
│   ├── LLMframework.png    # Live application screenshot
│   └── CALMOutput.png      # Real-world query demo output
├── docs/               # Additional documentation
└── LICENSE             # MIT License
```

<br/>

---

## 🔮 Roadmap

- [ ] 🔗 Support for `.docx`, `.txt`, `.csv` file formats
- [ ] 💬 Multi-turn conversation memory (chat history)
- [ ] 🌐 LangSmith tracing integration for observability
- [ ] 📊 Source citation with page numbers in responses
- [ ] 🐳 Docker containerization for one-command deployment
- [ ] 🔑 Optional OpenAI / Groq API fallback mode

<br/>

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

<br/>

---

<div align="center">

**Designed & Built with 🔥 by a passionate AI Engineer**

*If this project helped you, consider giving it a ⭐ — it means a lot!*

</div>
