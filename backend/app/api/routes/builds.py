from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.build import Build, BuildStatus
from app.models.project import Project
from app.models.user import User
from app.schemas.build import BuildCreate, BuildRead
from app.services.codegen import CodegenService

router = APIRouter()
codegen_service = CodegenService()


@router.post("", response_model=BuildRead, status_code=status.HTTP_201_CREATED)
def create_build(
    payload: BuildCreate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> Build:
    project = (
        db.query(Project)
        .filter(Project.id == payload.project_id, Project.owner_id == current_user.id)
        .first()
    )
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    codegen_service.create_build_job(project_id=payload.project_id, target=payload.target)

    build = Build(
        project_id=payload.project_id,
        target=payload.target,
        status=BuildStatus.queued,
        log_output="Build job queued",
    )
    db.add(build)
    db.commit()
    db.refresh(build)
    return build
