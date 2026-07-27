from app.services.embedding_service import search_embeddings


def semantic_search(
    query: str,
    top_k: int = 5,
):
    """
    Perform semantic search on ChromaDB.

    Returns:
        {
            "documents": ...,
            "metadatas": ...,
            "distances": ...
        }
    """

    results = search_embeddings(
        query=query,
        top_k=top_k,
    )

    return results