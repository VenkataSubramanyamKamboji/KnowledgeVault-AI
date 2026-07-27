from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    JSON,
)
from datetime import datetime

from app.database.database import Base


class KnowledgeItem(Base):
    __tablename__ = "knowledge_items"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(String, nullable=False)

    source_type = Column(String, nullable=False)

    source_url = Column(String, nullable=True)

    raw_text = Column(Text, nullable=True)

    summary = Column(Text, nullable=True)

    ai_metadata = Column(
    JSON,
    nullable=True
)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )