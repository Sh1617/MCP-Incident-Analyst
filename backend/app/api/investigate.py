from fastapi import APIRouter

from backend.app.graphs.workflow import incident_graph
from backend.app.schemas.investigation import (
    InvestigationRequest,
    InvestigationResponse
)

router = APIRouter(
    prefix="/investigate",
    tags=["Investigation"]
)


@router.post(
    "",
    response_model=InvestigationResponse
)
async def investigate(
    request: InvestigationRequest
):

    result = await incident_graph.ainvoke(
        {
            "user_query": request.query,
            "incident_id": "INC-001",
            "logs": [],
            "github_results": [],
            "db_results": [],
            "documentation_results": [],
            "findings": [],
            "confidence_score": 0.0,
            "final_report": ""
        }
    )

    return InvestigationResponse(
        report=result["final_report"],
        confidence_score=result["confidence_score"]
    )