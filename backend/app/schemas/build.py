from datetime import datetime

from pydantic import BaseModel, Field

from app.models.build import BuildStatus
from app.schemas.common import ORMModel


class BuildCreate(BaseModel):
    project_id: int
    target: str = Field(pattern="^(web|android)$")


class BuildRead(ORMModel):
    id: int
    project_id: int
    target: str
    status: BuildStatus
    artifact_url: str | None
    log_output: str | None
    created_at: datetime
