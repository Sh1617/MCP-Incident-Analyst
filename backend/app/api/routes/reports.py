from fastapi import APIRouter
from backend.app.mcp.manager import mcp_manager
from backend.app.repositories.investigation_repository import (
    InvestigationRepository
)

router = APIRouter()


@router.get("/reports")
async def get_reports():

    query = """
    SELECT
        id,
        report_id,
        confidence_score,
        created_at
    FROM reports
    ORDER BY created_at DESC
    """

    with mcp_manager.postgres.get_connection() as conn:

        with conn.cursor() as cur:

            cur.execute(query)

            rows = cur.fetchall()

    reports = []

    for row in rows:

        reports.append(
            {
                "id": row[0],
                "report_id": row[1],
                "confidence_score": row[2],
                "created_at": str(row[3])
            }
        )

    return {
        "reports": reports
    }

@router.get("/{report_id}")
async def get_report(
    report_id: str
):

    repo = InvestigationRepository()

    report = await repo.get_report(
        report_id
    )

    if report is None:

        return {
            "message": "Report not found"
        }

    return report