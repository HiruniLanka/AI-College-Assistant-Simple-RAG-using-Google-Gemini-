"""
rag_service.py

Main RAG Orchestrator
"""

from agents.retrieval_agent import RetrievalAgent
from agents.answer_agent import AnswerAgent


class RAGService:

    def __init__(self, retrieval_agent, answer_agent):

        self.retrieval_agent = retrieval_agent
        self.answer_agent = answer_agent

    def ask(self, question):
        """
        Complete RAG Pipeline

        Question
            ↓
        Retrieval Agent
            ↓
        Retrieved Context
            ↓
        Answer Agent
            ↓
        Final Answer
        """

        # Step 1
        retrieved_chunks = self.retrieval_agent.retrieve(question)

        # Step 2
        answer = self.answer_agent.generate_answer(
            question,
            retrieved_chunks
        )

        return answer