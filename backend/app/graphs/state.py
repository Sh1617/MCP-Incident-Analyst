from typing import TypedDict


class IncidentState(TypedDict):

    user_query: str

    incident_id: str

    logs: list

    github_results: list

    db_results: list

    documentation_results: list

    findings: list

    confidence_score: float

    final_report: str

    agent_metrics: dict