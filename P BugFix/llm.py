from config import Config
from openai import OpenAI

client = OpenAI(
    api_key=Config.OPENAI_API_KEY
)

model = Config.OPENAI_MODEL