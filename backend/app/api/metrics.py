from fastapi import APIRouter

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

agent_metrics = {}


@router.get("/")
async def get_metrics():

    return {
        "metrics": agent_metrics
    }