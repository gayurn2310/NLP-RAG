import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_groq.chat_models import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate

load_dotenv()  

PDF_PATH = os.path.join(os.path.dirname(__file__), "../data/NLP textbook.pdf")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "../chroma_db")

def setup_rag(pdf_path: str = PDF_PATH, persist_dir: str = CHROMA_DIR):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    db.persist()
    return db

def create_qa_chain(db: Chroma, model_name: str = "llama-3.3-70b-versatile"):
    llm = ChatGroq(model_name=model_name, temperature=0.0)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    template = """
    You are an assistant for answering questions based only on the provided context from the NLP textbook.
    If the answer cannot be found in the context, say:
    "Sorry, I don’t know. My knowledge is limited to the NLP textbook."

    Question: {question}

    Context:
    {context}

    Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question", "context"])

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )
    return qa