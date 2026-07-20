"""
config.py

Loads environment variables and project configuration.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==========================
# Gemini Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini model for chat
GEMINI_MODEL = "gemini-3.5-flash"

# Gemini embedding model
EMBEDDING_MODEL = "gemini-embedding-001"

# ==========================
# Vector Database
# ==========================

VECTOR_DB_NAME = "college_rules"

# Number of documents to retrieve
TOP_K = 3

# ==========================
# Document Settings
# ==========================

DOCUMENT_PATH = "documents/college_rules.txt"

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# ==========================
# Validation
# ==========================

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please create a .env file."
    )