from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import ORMModel


class AppSpecCreate(BaseModel):
    project_id: int
    prompt: str = Field(min_length=1)


class AppSpecRead(ORMModel):
    id: int
    project_id: int
    prompt: str
    generated_spec: str
    created_at: datetime
