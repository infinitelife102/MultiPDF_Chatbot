import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores.faiss import FAISS

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    # Use smaller chunks to stay within the LLM/embedding context window
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,      # max characters per chunk
        chunk_overlap=1000,    # overlap for better context continuity
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = OllamaEmbeddings(model="qwen3-embedding")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatOllama(model="llama3.1:8b", temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = OllamaEmbeddings(model="qwen3-embedding")
    new_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,  # safe here because the index is created locally by this app
    )
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])




def main():
    st.set_page_config(page_title="Multi-PDF Chatbot", page_icon=":scroll:")
    st.header("Multi-PDF Chatbot (RAG-based)")

    user_question = st.text_input("Ask a Question from the PDF Files uploaded...")

    if user_question:
        user_input(user_question)

    with st.sidebar:

        st.image("img/Robot.jpg")
        st.write("---")
        
        st.title("📁 PDF File's Section")
        pdf_docs = st.file_uploader("Upload your PDF Files & \n Click on the Submit & Process Button ", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file.")
                return
            with st.spinner("Processing..."): # user friendly message.
                raw_text = get_pdf_text(pdf_docs) # get the pdf text
                text_chunks = get_text_chunks(raw_text) # get the text chunks
                get_vector_store(text_chunks) # create vector store
                st.success("Done")
        
        st.write("---")
        st.image("img/gkj.jpg")
        st.write("Multi-PDF Chatbot")


    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
            Multi-PDF Chatbot
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
