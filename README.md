# Multi-PDF-s 📚ChatApp AI Agent 🤖

Meet MultiPDF Chat AI App! 🚀 Chat seamlessly with Multiple PDFs using LangChain, a local Ollama LLM (`llama3.1:8b`) &amp; FAISS Vector DB with seamless Streamlit deployment. Get instant, accurate responses from a privacy‑friendly local language model. 📚💬 Transform your PDF experience now! 🔥✨

## 📝 Description
The Multi-PDF's Chat Agent is a Streamlit-based web application designed to facilitate interactive conversations with a chatbot. The app allows users to upload multiple PDF documents, extract text information from them, and train a chatbot using this extracted content. Users can then engage in real-time conversations with the chatbot.

## 💻 Demo:
![Demo 1: Chatbot Output](img/LLMframework.jpg)

## 🎯 How It Works:
------------

![MultiPDF Chat App Diagram](img/Architecture.jpg)

The application follows these steps to provide responses to your questions:

1. **PDF Loading** : The app reads multiple PDF documents and extracts their text content.

2. **Text Chunking** : The extracted text is divided into smaller chunks that can be processed effectively.

3. **Language Model** : The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. **Similarity Matching** : When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. **Response Generation** : The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

![Demo 2: Chatbot Output](img/LLMApp.jpg)

--- 
## 🎯 Key Features

- **Adaptive Chunking**: Our Sliding Window Chunking technique dynamically adjusts window size and position for RAG, balancing fine-grained and coarse-grained data access based on data complexity and context.

- **Multi-Document Conversational QA**: Supports simple and multi-hop queries across multiple documents simultaneously, breaking the single-document limitation.

- **File Compatibility**: Supports both PDF and TXT file formats.

- **LLM Model Compatibility**: Supports Google Gemini Pro, OpenAI GPT 3, Anthropic Claude, Llama2 and other open-source LLMs.


![Demo 3: Chatbot Output](img/LLMAgents.jpg)


## 🌟Requirements

- **Python 3.9+** : Tested with recent Python 3.x versions.
- **Streamlit** : Web UI framework for building interactive apps.
- **LangChain** : For text splitting, RAG, vector stores, and LLM orchestration.
- **langchain‑community** : Community integrations, including `ChatOllama` and `OllamaEmbeddings`.
- **langchain‑text‑splitters** : Provides `RecursiveCharacterTextSplitter` used for chunking PDF text.
- **PyPDF2** : To extract text content from PDF files.
- **faiss‑cpu** : Vector database for efficient similarity search over PDF chunks.
- **Ollama** (desktop/server) : Local LLM runtime; this project uses the `llama3.1:8b` model via Ollama.

![Demo 4: Chatbot Output](img/CALMOutput.jpg)
---

## ▶️Installation

### 1. Create and activate a virtual environment (recommended)

```bash
cd Multi-PDFs_ChatApp_AI-Agent
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install the required Python packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Install and prepare Ollama (local LLM)

1. Install Ollama from the official website.
2. Start the Ollama server:

   ```bash
   ollama serve
   ```

3. Download the model used by this app:

   ```bash
   ollama pull llama3.1:8b
   ```

> 🔑 **Environment variables / .env**  
> This version does **not** use the Google Gemini API, so `GOOGLE_API_KEY` and a `.env` file are **not required**.  
> As long as Ollama is installed and running, the app will work without any additional API keys.

### 4. Run the Streamlit app

```bash
streamlit run chatapp.py
```

---
## 💡Usage

To use the Multi-PDF-s 📚ChatApp AI Agent 🤖, U can have glimpse of look by clicking on this link : [Launch App On Streamlit](https://multi-pdfschatappai-agent.streamlit.app/). To run app, fork app and follow the below steps to start using it. Use the sidebar to upload PDF files and train the chatbot. Once trained, you can have conversations with the chatbot by entering questions in the text input field.

In case You want to run & implement project on your system then follow these steps:

1. Ensure that you have installed the required dependencies via `pip install -r requirements.txt` and that **Ollama is running with the `llama3.1:8b` model pulled**.
2. Run the `chatapp.py` file using the Streamlit CLI. Execute the following command:
   ```bash
   streamlit run chatapp.py
   ```
3. The application will launch in your default web browser, displaying the user interface.
4. Upload multiple PDF documents into the app by following the provided instructions at sidebar. On the sidebar, you'll find an option to upload PDF documents. Click on the "Upload your documents here and click on Process" button and select one or more PDF files. 
5. Don't forget to click on Submit & Process Button.
6. Ask questions in natural language about the loaded PDFs using the chat interface.
7. Chatting with the Documents: After uploading and processing the PDF documents, you can ask questions by typing them in the text input field. Press Enter or click the "Ask" button to submit your question.

The application will use conversational AI to provide responses based on the content of the uploaded documents. The responses will be displayed in the chat interface.

---
## ©️ License 🪪 

This project is distributed under the MIT License. See `LICENSE` for more information.
