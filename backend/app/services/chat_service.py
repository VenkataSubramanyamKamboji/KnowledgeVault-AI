from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.services.search_service import semantic_search
from app.services.ai_service import answer_with_context


def chat(
    db: Session,
    question: str,
    top_k: int = 3,
):
    try:
        results = semantic_search(question, top_k)
    except Exception as e:
        raise HTTPException(
        status_code=500,
        detail=f"Search failed: {str(e)}"
    )

    # print("\n===== SEARCH RESULTS =====")
    # print(results)
    # print("==========================")

    documents = results.get("documents", [[]])[0]

    # print("Documents:")
    # print(documents)

    valid_documents = [
        doc
        for doc in documents
        if isinstance(doc, str) and doc.strip()
    ]

    if not valid_documents:
        return {
            "answer": "No relevant knowledge found.",
            "sources": [],
        }

    context = "\n\n".join(valid_documents)

    try:
        answer = answer_with_context(question, context)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate answer: {str(e)}"
    )

    metadata = results.get("metadatas", [[]])[0]

    sources = list({
        item["title"]
        for item in metadata
        if item and "title" in item
    })

    return {
        "answer": answer,
        "sources": sources,
    }