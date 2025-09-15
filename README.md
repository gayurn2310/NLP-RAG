# 📚 NLP Textbook RAG Chatbot

This project is an end-to-end **Retrieval-Augmented Generation (RAG) chatbot** that answers questions **only from an NLP textbook PDF**.  
It has two main parts:
- **Frontend (React + Vite + Tailwind + DaisyUI)**: A chat interface for users to ask questions.
- **Backend (FastAPI + LangChain + Chroma + Groq + HuggingFace)**: A RAG pipeline that loads the textbook, embeds it, stores it in a vector DB, retrieves relevant chunks, and uses Groq’s LLaMA model to generate answers.

---

## ✨ Features
### Frontend
- 📱 Chat-like interface (with DaisyUI components)  
- 🤖 Displays answers from the NLP textbook  

### Backend
- 📄 Loads and chunks **NLP textbook PDF**  
- 🔎 Stores embeddings in **Chroma vector database**  
- 🧠 Uses **HuggingFace MiniLM** embeddings  
- ⚡ Queries **Groq-hosted LLaMA 3.3 70B** for answer generation  
- ❌ Rejects out-of-scope questions (only answers from the textbook)  
- 🌐 Exposes a `/ask` FastAPI endpoint  

---

## 🛠️ Tech Stack
- **Frontend**: React, Vite, TailwindCSS, DaisyUI  
- **Backend**: FastAPI, LangChain, HuggingFace, Chroma, Groq API  
- **Vector DB**: Chroma (local persistence)  
- **Models**:
  - Embeddings: `all-MiniLM-L6-v2` (HuggingFace)  
  - LLM: `llama-3.3-70b-versatile` (Groq)  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/gayurn2310/NLP-RAG.git
cd NLP-RAG
```
### 2️⃣ Environment Variables Setup
Create a .env file in /backend with:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3️⃣ Backend Setup
``` bash
cd backend
uvicorn model.main:app --reload --port 8000
```
Backend will be live at http://localhost:8000.

### 4️⃣ Frontend Setup
``` bash
cd frontend
npm install
npm run dev
```
The frontend should be running at http://localhost:5173.
