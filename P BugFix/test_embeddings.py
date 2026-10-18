from embeddings import EmbeddingGenerator

generator = EmbeddingGenerator()

text = """
Machine Learning is a branch of Artificial Intelligence.
"""

embedding = generator.generate_embedding(text)

print("Embedding Length:", len(embedding))

print()

print("First 10 Values")

print(embedding[:10])