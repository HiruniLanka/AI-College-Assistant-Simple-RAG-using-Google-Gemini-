# AI College Assistant (Simple RAG)

A simple Retrieval-Augmented Generation (RAG) application built with Python and Google Gemini. It answers college-related questions using a local knowledge base and semantic search.

## Features

- Read knowledge from a text file
- Split documents into chunks
- Generate embeddings using Gemini Embedding
- Store embeddings in an in-memory vector database
- Retrieve relevant information using cosine similarity
- Generate answers using Gemini 3.5 Flash

## Tech Stack

- Python
- Google Gemini API
- Gemini 3.5 Flash
- Gemini Embedding 001
- Python Dotenv

## Project Structure

```text
college-rag/
├── agents/
├── services/
├── documents/
├── app.py
├── config.py
├── .env
└── README.md
```

## Run the Project

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

3. Run the application

```bash
python app.py
```

## Workflow

```
Knowledge Base
      ↓
Document Chunking
      ↓
Generate Embeddings
      ↓
Store in Vector DB
      ↓
User Question
      ↓
Retrieve Relevant Chunks
      ↓
Gemini Generates Answer
      ↓
Display Response
```

## Example

**Question:**
```
When does the library open?
```

**Answer:**
```
The library opens from 8 AM to 6 PM.
```

## Future Improvements

- TurboVec integration
- PDF/DOCX support
- Web interface
- Persistent vector database
- Chat history

## License

Educational project for learning Retrieval-Augmented Generation (RAG).
