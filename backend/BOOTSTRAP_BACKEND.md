# Prompt2App Studio Backend Bootstrap

This document defines the backend foundation for Prompt2App Studio, a SaaS platform that turns natural-language product ideas into implementation-ready specs and generated applications.

## Backend Goals

- Provide secure authentication and tenant-safe API access.
- Model core entities for projects, specs, and build pipelines.
- Expose clear, typed API contracts for frontend and automation flows.
- Keep architecture modular, testable, and production-ready.

## Tech Stack

- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- PostgreSQL
- JWT authentication with bcrypt password hashing

## Backend Folder Structure

```text
backend/
└─ app/
	├─ api/       # Route modules and API wiring
	├─ core/      # Settings, security, and shared backend config
	├─ db/        # Engine/session setup and declarative base
	├─ models/    # SQLAlchemy domain models
	├─ schemas/   # Pydantic request and response schemas
	└─ services/  # Business services (LLM orchestration, codegen)
```

## Initial Scope

- Main app entrypoint with CORS for frontend development origin.
- Centralized settings and environment-driven configuration.
- Database engine/session management and base model registration.
- Security helpers for password hashing and JWT token handling.
- Core models and schemas: User, Project, AppSpec, Build.
- API routers: auth, projects, specs, builds.
- Service stubs: LLMService and CodegenService.

## Engineering Standards

- Strong typing throughout Python code.
- Clear error handling and secure defaults.
- No unused imports, dead code, or failing placeholders.
- Code should compile, run, and align with FastAPI best practices.

## Local Setup

1. Start PostgreSQL:

	```bash
	docker compose up -d postgres
	```

2. Create backend environment file:

	```bash
	cp .env.example .env
	```

	On Windows PowerShell:

	```powershell
	Copy-Item .env.example .env
	```

3. Run migrations:

	```bash
	python -m alembic upgrade head
	```

4. Start API:

	```bash
	uvicorn app.main:app --reload
	```