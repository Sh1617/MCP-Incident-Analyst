from typing import TypedDict
from typing import List
from typing import Optional


class IncidentState(TypedDict):

    user_query: str

    incident_id: Optional[str]

    logs: List

    github_results: List

    db_results: List

    documentation_results: List

    findings: List

    confidence_score: float

    final_report: str