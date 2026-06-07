from backend.app.agents.base_agent import BaseAgent
from backend.app.llm.factory import LLMFactory
from backend.app.core.metrics import AgentTimer
from backend.app.core.logger import get_logger


logger = get_logger(__name__)


class RCAAgent(BaseAgent):

    name = "rca_agent"

    def __init__(self):

        self.llm = LLMFactory.get_llm()

    async def execute(self, state):

        timer = AgentTimer()
        timer.start()

        logger.info(
            "RCA Agent Started"
        )

        logs = str(
            state.get("logs", [])
        )[:150]

        db_results = str(
            state.get("db_results", [])
        )[:100]

        docs = str(
            state.get(
                "documentation_results",
                []
            )
        )[:150]

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

Analyze the incident and generate a concise RCA.

User Query:
{state.get("user_query")}

Logs:
{logs}

Historical Incidents:
{db_results}

Documentation:
{docs}

Recent Code Changes:
{commit_summary}

Generate:

1. Executive Summary
2. Root Cause
3. Impact Analysis
4. Remediation Steps
5. Confidence Score

Keep the response under 300 words.
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

        state["confidence_score"] = 0.85

        if "agent_metrics" not in state:

            state["agent_metrics"] = {}

        state["agent_metrics"][
            self.name
        ] = timer.stop()

        logger.info(
            f"RCA Agent Finished | "
            f"Execution Time={state['agent_metrics'][self.name]}s"
        )

        return state