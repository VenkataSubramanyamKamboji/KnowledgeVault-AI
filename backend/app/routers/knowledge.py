from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.knowledge import (
    KnowledgeCreate,
    KnowledgeUpdate,
    KnowledgeResponse
)
from app.services.knowledge_service import (
    create_knowledge,
    get_user_knowledge,
    get_knowledge_by_id,
    update_knowledge,
    delete_knowledge
)
from typing import List

router = APIRouter(
    prefix="/api/v1/knowledge",
    tags=["Knowledge"]
)


@router.post("/", response_model=KnowledgeResponse)
def save_knowledge(
    knowledge: KnowledgeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_knowledge(
        db,
        knowledge,
        current_user
    )

@router.get("/", response_model=List[KnowledgeResponse])
def get_knowledge(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_knowledge(
        db,
        current_user
    )

@router.get("/{knowledge_id}", response_model=KnowledgeResponse)
def get_single_knowledge(
    knowledge_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    knowledge = get_knowledge_by_id(
        db,
        knowledge_id,
        current_user
    )

    if knowledge is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    return knowledge

@router.put("/{knowledge_id}", response_model=KnowledgeResponse)
def update_single_knowledge(
    knowledge_id: int,
    knowledge_update: KnowledgeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = update_knowledge(
        db,
        knowledge_id,
        knowledge_update,
        current_user
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    return updated

@router.delete("/{knowledge_id}")
def delete_single_knowledge(
    knowledge_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = delete_knowledge(
        db,
        knowledge_id,
        current_user
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    return {
        "message": "Knowledge deleted successfully"
    }