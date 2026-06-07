from backend.app.agents.base_agent import BaseAgent
from backend.app.llm.factory import LLMFactory
from backend.app.core.metrics import AgentTimer
from backend.app.core.logger import get_logger
from backend.app.core.tracing import tracer
from backend.app.repositories.investigation_repository import (
    InvestigationRepository
)
from backend.app.api.metrics import (
    agent_metrics
)

logger = get_logger(__name__)


class RCAAgent(BaseAgent):

    name = "rca_agent"

    def __init__(self):

        self.llm = LLMFactory.get_llm()

    async def execute(self, state):

        with tracer.start_as_current_span(
            "rca_agent_execution"
        ):

            timer = AgentTimer()
            timer.start()

            logger.info(
                "RCA Agent Started"
            )

            logs = str(
                state.get("logs", [])
            )[:300]

            db_results = str(
                state.get("db_results", [])
            )[:200]

            docs = str(
                state.get(
                    "documentation_results",
                    []
                )
            )[:300]

            commit_summary = "\n".join(
                [
                    commit["message"]
                    for commit in state.get(
                        "github_results",
                        []
                    )[:3]
                ]
            )

            prompt = f"""
You are a Senior Site Reliability Engineer.

IMPORTANT RULES:

1. Use ONLY the supplied evidence.
2. Do NOT invent outages.
3. Do NOT assume financial loss.
4. Do NOT assume customer impact unless evidence exists.
5. If evidence is insufficient, state:
   "Insufficient evidence to determine root cause."

User Query:
{state.get("user_query")}

Evidence:

Logs:
{logs}

Historical Incidents:
{db_results}

Documentation:
{docs}

Recent Code Changes:
{commit_summary}

Generate the following sections:

Executive Summary

Evidence Collected

Root Cause

Impact Analysis

Remediation Steps

Confidence Score

Keep the response under 250 words.
"""

            logger.info(
                f"RCA Prompt Length={len(prompt)}"
            )

            response = self.llm.invoke(
                prompt
            )

            logger.info(
                "LLM Response Received"
            )

            state["final_report"] = (
                response.content
            )

            confidence = 0.50

            if state.get("logs"):
                confidence += 0.20

            if state.get("db_results"):
                confidence += 0.15

            if state.get("github_results"):
                confidence += 0.15

            state["confidence_score"] = min(
                confidence,
                1.0
            )

            if "agent_metrics" not in state:

                state["agent_metrics"] = {}

            state["agent_metrics"][
                self.name
            ] = timer.stop()

            repo = InvestigationRepository()

            await repo.save_report(
                state["final_report"],
                state["confidence_score"]
            )

            logger.info(
                "RCA Report Saved"
            )

            logger.info(
                f"Confidence Score={state['confidence_score']}"
            )

            logger.info(
                f"RCA Agent Finished | "
                f"Execution Time={state['agent_metrics'][self.name]}s"
            )

            agent_metrics.update(
                state.get(
                    "agent_metrics",
                    {}
                )
            )

            return state