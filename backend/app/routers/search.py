from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.search import SearchRequest
from app.services.search_service import semantic_search

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


@router.post("/")
def search(
    request: SearchRequest,
    db: Session = Depends(get_db),
):
    return semantic_search(
        db,
        request.query,
        request.top_k,
    )