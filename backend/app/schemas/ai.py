from pydantic import BaseModel


class AIResponse(BaseModel):
    summary: str
    key_points: list[str]
    tags: list[str]