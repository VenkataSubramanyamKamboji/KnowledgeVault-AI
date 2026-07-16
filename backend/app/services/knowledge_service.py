from sqlalchemy.orm import Session

from app.models.knowledge import KnowledgeItem
from app.schemas.knowledge import (
    KnowledgeCreate,
    KnowledgeUpdate,
    URLRequest
)
from app.models.user import User
from app.extractors.factory import get_extractor
from app.utils.url_detector import detect_source_type
from app.services.ai_service import generate_summary

def create_knowledge(
    db: Session,
    knowledge: KnowledgeCreate,
    current_user: User
):
    new_item = KnowledgeItem(
        user_id=current_user.id,
        title=knowledge.title,
        source_type=knowledge.source_type,
        source_url=knowledge.source_url,
        raw_text=knowledge.raw_text
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

def get_user_knowledge(
    db: Session,
    current_user: User
):
    return (
        db.query(KnowledgeItem)
        .filter(KnowledgeItem.user_id == current_user.id)
        .all()
    )

def get_knowledge_by_id(
    db: Session,
    knowledge_id: int,
    current_user: User
):
    return (
        db.query(KnowledgeItem)
        .filter(
            KnowledgeItem.id == knowledge_id,
            KnowledgeItem.user_id == current_user.id
        )
        .first()
    )

def update_knowledge(
    db: Session,
    knowledge_id: int,
    knowledge_update: KnowledgeUpdate,
    current_user: User
):
    knowledge = (
        db.query(KnowledgeItem)
        .filter(
            KnowledgeItem.id == knowledge_id,
            KnowledgeItem.user_id == current_user.id
        )
        .first()
    )

    if knowledge is None:
        return None

    knowledge.title = knowledge_update.title
    knowledge.source_type = knowledge_update.source_type
    knowledge.source_url = knowledge_update.source_url
    knowledge.raw_text = knowledge_update.raw_text

    db.commit()
    db.refresh(knowledge)

    return knowledge

def delete_knowledge(
    db: Session,
    knowledge_id: int,
    current_user: User
):
    knowledge = (
        db.query(KnowledgeItem)
        .filter(
            KnowledgeItem.id == knowledge_id,
            KnowledgeItem.user_id == current_user.id
        )
        .first()
    )

    if knowledge is None:
        return False

    db.delete(knowledge)
    db.commit()

    return True

def create_knowledge_from_url(
    db: Session,
    url_request: URLRequest,
    current_user: User
):
    extractor = get_extractor(
        url_request.url
    )

    extracted_data = extractor.extract(
        url_request.url
    )
    summary = generate_summary(
    extracted_data["raw_text"]
)
    source_type = detect_source_type(
    url_request.url
)

    knowledge = KnowledgeItem(
        title=extracted_data["title"],
        source_type=source_type,
        source_url=url_request.url,
        raw_text=extracted_data["raw_text"],
        summary=summary,
        user_id=current_user.id
    )

    db.add(knowledge)
    db.commit()
    db.refresh(knowledge)

    return knowledge