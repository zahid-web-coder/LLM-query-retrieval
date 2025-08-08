# LLM-Powered Legal Query–Retrieval System 🔍📄

A Streamlit-based intelligent assistant that answers queries about legal documents using LLMs and semantic search. It highlights relevant clauses in PDFs and explains them in context — powered by Gemini API.

---

## 🚀 Features

- 🔎 **Semantic Clause Search** — Retrieves most relevant sections from a legal document using FAISS + embeddings.
- 📄 **PDF Clause Highlighting** — Highlights matched clauses in the original PDF using PyMuPDF.
- 💡 **LLM Explanation** — Explains the retrieved clauses using Gemini/GPT APIs.
- 🧠 **Final Decision Inference** — Outputs a yes/no/maybe decision with reasoning.
- 📤 **Downloadable Outputs** — Option to download structured JSON and annotated PDF.

---

## 🖥️ Demo

Check out the live demo 👉 [Streamlit App](https://techbytesllmproject.streamlit.app/)

---

## 🗂️ Folder Structure
```
llm_query_app/
├── app.py # Streamlit UI and logic
├── requirements.txt # Python dependencies
├── README.md # Project overview
├── test_gemini.py # LLM test script
├── data/
│ └── all_chunks.jsonl # Pre-processed document chunks
├── vector_index/
│ └── faiss_index.index # Vector DB for retrieval
└── utils/
├── document_loader.py # Loads and processes documents
├── vector_search.py # FAISS-based search
├── llm_explainer.py # Gemini prompt and response logic
├── pdf_highlighter.py # Highlights clauses in PDFs
├── decision_engine.py # Decision logic based on LLM
```

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/llm-query-retrieval.git
cd llm_query_app
```
---
### Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
---
### Install dependencies
```bash
pip install -r requirements.txt
```
---
### Run the app
```bash
streamlit run app.py
```
---
### 🔐 Environment Setup
Create a .env file or set your environment variables for:

```ini
GEMINI_API_KEY=your_api_key_here
```
---

## 📄 Input/Output
Input: PDF document + user query

## Output:

Top matching clause(s)

Explanation by LLM

Final decision (Yes/No/Maybe)

Highlighted PDF download

Raw JSON output

---

## 🧠 LLM Backend
 Gemini Pro (via API)

 Token-level prompt customization

 Support for GPT-4 (optional future integration)

 ---

## 📦 Future Improvements
Upload custom PDFs directly via UI

Add feedback/rating system per clause

Switchable models: GPT / Gemini / Ollama

MongoDB storage for user queries & analytics

---

## 👨‍💻 Contributors
Zahid Mohammed — Full Stack + AI Developer

---

