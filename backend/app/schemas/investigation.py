from pydantic import BaseModel


class InvestigationRequest(BaseModel):
    query: str


class InvestigationResponse(BaseModel):
    report: str
    confidence_score: float