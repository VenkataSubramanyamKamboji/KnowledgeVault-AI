# from pydantic import BaseModel
# from typing import Optional, Any


# class KnowledgeCreate(BaseModel):
#     title: str
#     source_type: str
#     source_url: Optional[str] = None
#     raw_text: Optional[str] = None


# class KnowledgeResponse(BaseModel):
#     id: int

#     title: str

#     source_type: str

#     source_url: Optional[str]

#     raw_text: Optional[str]

#     summary: Optional[str]

#     ai_metadata: Optional[dict[str, Any]] = None

#     model_config = {
#         "from_attributes": True
#     }


# class KnowledgeUpdate(BaseModel):
#     title: str
#     source_type: str
#     source_url: Optional[str] = None
#     raw_text: Optional[str] = None

# class URLRequest(BaseModel):
#     url: str

from pydantic import BaseModel
from typing import Optional, Any


class KnowledgeCreate(BaseModel):
    title: str
    source_type: str
    source_url: Optional[str] = None
    raw_text: Optional[str] = None


class KnowledgeResponse(BaseModel):
    id: int
    title: str
    source_type: str
    source_url: Optional[str]
    raw_text: Optional[str]
    summary: Optional[str]
    ai_metadata: Optional[dict[str, Any]] = None

    model_config = {
        "from_attributes": True
    }


class KnowledgeUpdate(BaseModel):
    title: str
    source_type: str
    source_url: Optional[str] = None
    raw_text: Optional[str] = None


class URLRequest(BaseModel):
    url: str