
# 📄 QA with Documents (Text) using Gemini + LlamaIndex

This project enables **question-answering (QA)** on uploaded documents using Google **Gemini Pro LLM**, **Gemini Embeddings**, and **LlamaIndex**. A user-friendly interface is provided via **Streamlit** to allow natural language querying of any uploaded PDF, TXT, or Markdown file.

---

## 🚀 Features

- ✅ Upload PDF, TXT, or MD files via Streamlit UI  
- ✅ Extracts and indexes content using `LlamaIndex`  
- ✅ Embeds text using `GeminiEmbedding`  
- ✅ Answers questions with Google's `Gemini-Pro` LLM  
- ✅ Logs all key steps and errors for debugging  
- ✅ Modular codebase with `data_ingestion`, `embedding`, `model_api`, and `app` separation  

---

## 🛠️ Tech Stack

- [LlamaIndex](https://www.llamaindex.ai/)
- [Google Generative AI SDK](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [Python 3.10+](https://www.python.org/)
- Modular Python architecture using custom `exception` and `logger` modules

---

## 📁 Project Structure

```
QAWithPDF/
│
├── App.py                  # Streamlit app
├── data_ingestion.py       # Document loading
├── embedding.py            # Embedding + indexing
├── model_api.py            # Gemini model loader
├── exception.py            # Custom exception handling
├── logger.py               # Logging configuration
├── __init__.py             # Optional package marker
├── requirements.txt        # Required dependencies
├── .env                    # Contains your Google API Key
└── Data/                   # Uploaded files directory (auto-created)
```

---

## ⚙️ Setup Instructions

### 1. ✅ Clone the repository

```bash
git clone https://github.com/your-username/QAWithPDF.git
cd QAWithPDF
```

### 2. ✅ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ✅ Set your API key in a `.env` file

Create a `.env` file in the root with:

```
GOOGLE_API_KEY=your_google_genai_api_key
```

### 5. ✅ Run the app

```bash
streamlit run App.py
```

---

## 📦 requirements.txt

```txt
llama-index>=0.10.28
google-generativeai
streamlit
python-dotenv
ipython
tqdm
```

---

## 💡 Example Questions You Can Ask

- “What is this document about?”
- “What are the differences between supervised and unsupervised learning?”
- “Summarize this file in 3 bullet points.”

---

## 🛡️ Notes

- `ServiceContext` is deprecated – we use `Settings` from `llama_index.core.settings`.
- Works with Google’s `gemini-pro` and `embedding-001` models.

---

## 🙌 Acknowledgments
- [Suuny Savita] (https://www.youtube.com/watch?v=hqJxgbxczOo&list=PLQxDHpeGU14Blorx3Ps1eZJ4XvKET1_vx)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Google Gemini SDK](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
