# Custom Knowledge Base Chatbot 

This project is a chatbot powered by **LangChain**, **FAISS**, and **Gemini (Google Generative AI)**. It can answer user questions based on a custom text document using retrieval-augmented generation (RAG).

---

##  Features

- Answers questions using only your uploaded knowledge base (`smart_homes_info.txt`)
- Uses **HuggingFace embeddings** + **FAISS** for fast semantic search
- Integrated with **Gemini 1.5 Flash** for high-quality responses
- Simple and clean **Streamlit web UI**
- Environment-safe using `.env` for API keys

---

##  Technologies Used

| Tool / Technology            | Purpose                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| **Python**                   | Core programming language                                               |
| **LangChain**                | Framework for building LLM + retrieval chains                           |
| **Google Gemini API**        | Large Language Model (LLM) to generate human-like responses             |
| **FAISS**                    | Vector database for fast document retrieval based on similarity         |
| **HuggingFace Transformers** | Used for text embeddings (`all-MiniLM-L6-v2`)                           |
| **Streamlit**                | Frontend UI framework for building the chatbot interface                |
| **python-dotenv**            | Securely load environment variables from a `.env` file                  |
| **VS Code**                  | IDE used for code editing and debugging                                 |
| **GitHub**                   | Source code hosting and version control                                 |

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/custom-knowledge-chatbot.git
cd custom-knowledge-chatbot
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
.env\Scriptsctivate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=custom-knowledge-chatbot
```

>  Never commit your real `.env` file — only use `.env.example` for sharing!

---

##  Files

| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `chatbot.py`          | Streamlit chatbot interface                      |
| `smart_homes_info.txt`| Sample custom data used as chatbot knowledge     |
| `.env.example`        | Template for environment configuration           |
| `requirements.txt`    | All dependencies for this project                |

---

##  Run the Chatbot

```bash
streamlit run chatbot.py
```

Then open: http://localhost:8501

---

##  Author

Keshwanth G P

---

##  License

This project is open source and free to use under the MIT License.
