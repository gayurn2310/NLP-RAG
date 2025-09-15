import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .rag import setup_rag, create_qa_chain
from fastapi.middleware.cors import CORSMiddleware

db = setup_rag()
qa_chain = create_qa_chain(db)

app = FastAPI(title="NLP Textbook Chatbot API")
origins = [
    "http://localhost:5173",  # replace with your frontend URL (Vite default)
    "http://localhost:3000",  # React default if using CRA
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(payload: dict):
    question = payload.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    result = qa_chain({"query": question})

    return {
        "answer": result["result"],
        "sources": [doc.metadata.get("source") for doc in result["source_documents"]],
    }

@app.get("/")
async def root():
    return {"message": "NLP Textbook Chatbot API is running!"}
