from config import Config
import chromadb

client = chromadb.PersistentClient(
    path=Config.CHROMA_PATH
)

collection = client.get_or_create_collection(
    Config.COLLECTION_NAME
)