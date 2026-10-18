"""
embeddings.py
-------------
Generate OpenAI Embeddings
"""

from openai import OpenAI
from config import Config


class EmbeddingGenerator:
    """
    Generate vector embeddings using OpenAI.
    """

    def __init__(self):

        if not Config.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found in .env file."
            )

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

        self.model = Config.EMBEDDING_MODEL

    def generate_embedding(self, text):
        """
        Generate embedding for one document.

        Parameters
        ----------
        text : str

        Returns
        -------
        list
        """

        if not text:
            return []

        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding

    def generate_embeddings(self, texts):
        """
        Generate embeddings for multiple documents.

        Parameters
        ----------
        texts : list

        Returns
        -------
        list
        """

        if not texts:
            return []

        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [
            item.embedding
            for item in response.data
        ]

    def cosine_similarity(self, vector1, vector2):
        """
        Calculate cosine similarity.
        """

        dot_product = sum(
            a * b
            for a, b in zip(vector1, vector2)
        )

        magnitude1 = sum(
            a * a
            for a in vector1
        ) ** 0.5

        magnitude2 = sum(
            b * b
            for b in vector2
        ) ** 0.5

        if magnitude1 == 0 or magnitude2 == 0:
            return 0

        return dot_product / (magnitude1 * magnitude2)


if __name__ == "__main__":

    generator = EmbeddingGenerator()

    text = """
    Artificial Intelligence is transforming the world.
    """

    embedding = generator.generate_embedding(text)

    print("=" * 60)
    print("Embedding Created Successfully")
    print("=" * 60)

    print(f"Dimensions : {len(embedding)}")

    print()

    print("First 10 Values")

    print(embedding[:10])