from fastapi import APIRouter

from backend.app.repositories.investigation_repository import (
    InvestigationRepository
)

router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"]
)


@router.get("/")
async def get_investigations():

    repo = InvestigationRepository()

    investigations = await (
        repo.get_investigations()
    )

    return {
        "investigations": investigations
    }