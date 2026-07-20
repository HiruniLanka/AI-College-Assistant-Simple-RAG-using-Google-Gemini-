"""
app.py

Main entry point for the AI College Assistant.
"""

from services.document_service import DocumentService
from services.embedding_service import EmbeddingService
from services.vector_db_service import VectorDBService
from services.rag_service import RAGService

from agents.retrieval_agent import RetrievalAgent
from agents.answer_agent import AnswerAgent

from config import (
    GEMINI_MODEL,
    EMBEDDING_MODEL,
    VECTOR_DB_NAME,
    DOCUMENT_PATH,
    TOP_K
)


def main():
    print("=" * 50)
    print("      AI College Assistant")
    print("=" * 50)

    print(f"Gemini Model      : {GEMINI_MODEL}")
    print(f"Embedding Model   : {EMBEDDING_MODEL}")
    print(f"Vector Database   : {VECTOR_DB_NAME}")
    print(f"Knowledge File    : {DOCUMENT_PATH}")
    print(f"Top K Results     : {TOP_K}")
    print()

    # ---------------------------------------
    # Initialize Services
    # ---------------------------------------

    print("Initializing services...")

    document_service = DocumentService()
    embedding_service = EmbeddingService()
    vector_db = VectorDBService()

    # ---------------------------------------
    # Load Knowledge Base
    # ---------------------------------------

    print("Loading knowledge base...")

    chunks = document_service.load_chunks()

    if not chunks:
        print("No document found or document is empty.")
        return

    print(f"Loaded {len(chunks)} chunks.")

    # ---------------------------------------
    # Generate Embeddings
    # ---------------------------------------

    print("Generating embeddings...")

    embedded_documents = embedding_service.generate_embeddings(chunks)

    # ---------------------------------------
    # Store in Vector Database
    # ---------------------------------------

    vector_db.add_documents(embedded_documents)

    print(f"Stored {vector_db.count()} vectors.")

    # ---------------------------------------
    # Create Agents
    # ---------------------------------------

    retrieval_agent = RetrievalAgent(
        vector_db,
        embedding_service
    )

    answer_agent = AnswerAgent()

    rag = RAGService(
        retrieval_agent,
        answer_agent
    )

    print("\nAI College Assistant is ready!")
    print("Type 'exit' to quit.\n")

    # ---------------------------------------
    # Chat Loop
    # ---------------------------------------

    while True:

        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            answer = rag.ask(question)
            print(f"\nAssistant: {answer}\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()