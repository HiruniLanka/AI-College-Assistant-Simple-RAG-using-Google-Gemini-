"""
document_service.py

Responsible for:
1. Reading the knowledge document
2. Splitting it into chunks
"""

from config import DOCUMENT_PATH


class DocumentService:

    def __init__(self):
        self.document_path = DOCUMENT_PATH

    def load_document(self):
        """
        Read the text file.
        """

        try:
            with open(self.document_path, "r", encoding="utf-8") as file:
                text = file.read()

            return text

        except FileNotFoundError:
            print("Document not found.")
            return ""

    def chunk_document(self, text):
        """
        Split document into chunks.

        Here we split using blank lines.
        Each paragraph becomes one chunk.
        """

        chunks = []

        paragraphs = text.split("\n\n")

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if paragraph:
                chunks.append(paragraph)

        return chunks

    def load_chunks(self):
        """
        Convenience method.

        Read the document and return chunks.
        """

        text = self.load_document()

        return self.chunk_document(text)