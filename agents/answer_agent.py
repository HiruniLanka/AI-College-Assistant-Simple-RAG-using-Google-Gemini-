"""
answer_agent.py

Responsible for generating answers using
Google Gemini and the retrieved context.
"""

from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL


class AnswerAgent:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_answer(self, question, retrieved_chunks):
        """
        Generate an answer using Gemini.
        """

        # Combine retrieved chunks into one context
        context = "\n\n".join(
            [chunk["text"] if isinstance(chunk, dict) else chunk
             for chunk in retrieved_chunks]
        )

        prompt = f"""
You are an AI College Assistant.

Answer the user's question ONLY using the provided context.

If the answer is not found in the context, reply:
"I couldn't find the answer in the college knowledge base."

--------------------
Context:
{context}

--------------------
Question:
{question}

Answer:
"""

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text.strip()