class RetrievalAgent:

    def __init__(self, vector_db, embedding_service):
        self.vector_db = vector_db
        self.embedding_service = embedding_service

    def retrieve(self, question):
        """
        Retrieve relevant chunks for the user's question.
        """

        question_embedding = self.embedding_service.generate_embedding(question)

        results = self.vector_db.search(question_embedding)

        return results