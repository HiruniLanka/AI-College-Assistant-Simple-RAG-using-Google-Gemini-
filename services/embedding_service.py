from google import genai
from config import GEMINI_API_KEY, EMBEDDING_MODEL


class EmbeddingService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_embedding(self, text):
        response = self.client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text
        )

        # New SDK format
        if hasattr(response, "embeddings"):
            return response.embeddings[0].values

        # Fallback
        return response.embedding.values

    def generate_embeddings(self, chunks):
        results = []

        for chunk in chunks:
            embedding = self.generate_embedding(chunk)

            results.append({
                "text": chunk,
                "embedding": embedding
            })

        return results