from backend.app.agents.base_agent import BaseAgent
from backend.app.llm.factory import LLMFactory
from backend.app.core.metrics import AgentTimer


class RCAAgent(BaseAgent):

    name = "rca_agent"

    def __init__(self):
        self.llm = LLMFactory.get_llm()

    async def execute(self, state):

        timer = AgentTimer()
        timer.start()

        print("RCA Agent Started")

        logs = str(
            state.get("logs", [])
        )[:500]

        db_results = str(
            state.get("db_results", [])
        )[:300]

        docs = str(
            state.get(
                "documentation_results",
                []
            )
        )[:500]

        github = str(
            state.get(
                "github_results",
                []
            )
        )[:300]

        prompt = f"""
You are a Site Reliability Engineer.

Analyze the evidence and generate a concise Root Cause Analysis.

User Query:
{state.get("user_query")}

Logs:
{logs}

Historical Incidents:
{db_results}

Documentation:
{docs}

GitHub Changes:
{github}

Provide:

1. Executive Summary
2. Root Cause
3. Impact
4. Remediation Steps
5. Confidence Score
"""

        print(
            "Prompt Length:",
            len(prompt)
        )

        response = self.llm.invoke(
            prompt
        )

        print(
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

        print(
            "RCA Agent Finished"
        )

        return state