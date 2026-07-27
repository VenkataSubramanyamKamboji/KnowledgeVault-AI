from sqlalchemy.orm import Session

from app.services.search_service import semantic_search
from app.services.ai_service import answer_with_context


def chat(
    db: Session,
    question: str,
    top_k: int = 3,
):
    results = semantic_search(
        query=question,
        top_k=top_k,
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

    answer = answer_with_context(
        question=question,
        context=context,
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