"""
vector_db_service.py

A simple in-memory vector database for learning RAG.
"""

import math
from config import TOP_K


class VectorDBService:

    def __init__(self):
        # Stores:
        # {
        #     "text": "...",
        #     "embedding": [...]
        # }
        self.documents = []

    def add_documents(self, documents):
        """
        Add embedded documents to the vector database.

        Parameters:
            documents (list)
        """

        self.documents.extend(documents)

    def cosine_similarity(self, vector1, vector2):
        """
        Calculate cosine similarity.
        """

        dot_product = sum(a * b for a, b in zip(vector1, vector2))

        magnitude1 = math.sqrt(sum(a * a for a in vector1))
        magnitude2 = math.sqrt(sum(b * b for b in vector2))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0

        return dot_product / (magnitude1 * magnitude2)

    def search(self, query_embedding, top_k=TOP_K):
        """
        Search the most similar documents.
        """

        similarities = []

        for document in self.documents:

            score = self.cosine_similarity(
                query_embedding,
                document["embedding"]
            )

            similarities.append({
                "text": document["text"],
                "score": score
            })

        similarities.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return similarities[:top_k]

    def count(self):
        """
        Number of stored documents.
        """
        return len(self.documents)