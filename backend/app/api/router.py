from fastapi import APIRouter

from app.api.routes import auth, builds, projects, specs

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(specs.router, prefix="/specs", tags=["specs"])
api_router.include_router(builds.router, prefix="/builds", tags=["builds"])
