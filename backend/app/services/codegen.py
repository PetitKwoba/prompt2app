class CodegenService:
    def create_build_job(self, project_id: int, target: str) -> dict[str, str | int]:
        return {"project_id": project_id, "target": target, "job_status": "queued"}
