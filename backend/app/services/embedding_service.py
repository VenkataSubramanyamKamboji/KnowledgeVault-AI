import os
from dotenv import load_dotenv
from google import genai

from app.vectorstore.chroma_db import collection

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

EMBEDDING_MODEL = "gemini-embedding-001"


def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding for a single piece of text.
    Used for search queries.
    """
    text = text[:10000]

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )

    return response.embeddings[0].values


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple chunks.
    Used while indexing documents.
    """

    if not texts:
        return []

    # Gemini accepts a list of contents
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=[text[:10000] for text in texts],
    )

    return [
        embedding.values
        for embedding in response.embeddings
    ]


def search_embeddings(
    query: str,
    top_k: int = 5,
):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    return results