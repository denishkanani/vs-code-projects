import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Application Configuration
    """

    # ==========================
    # OpenAI
    # ==========================
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "text-embedding-3-small"
    )

    # ==========================
    # Search
    # ==========================
    SEARCH_RESULTS = 5

    # ==========================
    # Scraper
    # ==========================
    REQUEST_TIMEOUT = 10

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )

    # ==========================
    # ChromaDB
    # ==========================
    CHROMA_PATH = "./chroma_db"
    COLLECTION_NAME = "research_documents"

    # ==========================
    # SQLite
    # ==========================
    DATABASE_NAME = "research.db"

    # ==========================
    # RAG
    # ==========================
    TOP_K_RESULTS = 3
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    # ==========================
    # FastAPI
    # ==========================
    HOST = "127.0.0.1"
    PORT = 8000
    DEBUG = True

    # ==========================
    # Uploads
    # ==========================
    UPLOAD_FOLDER = "uploads"

    ALLOWED_EXTENSIONS = [
        ".pdf",
        ".txt",
        ".docx"
    ]