from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatRequest
from app.services.chat_service import chat

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
def ask(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    return chat(
        db=db,
        question=request.question,
        top_k=request.top_k,
    )