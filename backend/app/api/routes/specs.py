from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.app_spec import AppSpec
from app.models.project import Project
from app.models.user import User
from app.schemas.app_spec import AppSpecCreate, AppSpecRead
from app.services.llm import LLMService

router = APIRouter()
llm_service = LLMService()


@router.post("", response_model=AppSpecRead, status_code=status.HTTP_201_CREATED)
def generate_spec(
    payload: AppSpecCreate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> AppSpec:
    project = (
        db.query(Project)
        .filter(Project.id == payload.project_id, Project.owner_id == current_user.id)
        .first()
    )
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    generated_spec = llm_service.generate_spec_from_prompt(payload.prompt)
    app_spec = AppSpec(project_id=payload.project_id, prompt=payload.prompt, generated_spec=generated_spec)
    db.add(app_spec)
    db.commit()
    db.refresh(app_spec)
    return app_spec
