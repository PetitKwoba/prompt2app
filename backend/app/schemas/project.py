from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import ORMModel


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = None


class ProjectRead(ORMModel):
    id: int
    owner_id: int
    name: str
    description: str | None
    created_at: datetime
