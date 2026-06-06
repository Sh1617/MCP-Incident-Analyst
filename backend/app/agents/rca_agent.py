from backend.app.agents.base_agent import BaseAgent
from backend.app.llm.factory import LLMFactory


class RCAAgent(BaseAgent):

    name = "rca_agent"

    def __init__(self):
        self.llm = LLMFactory.get_llm()

    async def execute(self, state):

        prompt = f"""
You are an expert Site Reliability Engineer.

Analyze the incident and generate a Root Cause Analysis.

User Query:
{state["user_query"]}

Log Findings:
{state["logs"]}

Historical Incident Data:
{state["db_results"]}

Documentation Findings:
{state["documentation_results"]}

Generate:

1. Executive Summary
2. Timeline
3. Evidence Collected
4. Root Cause
5. Contributing Factors
6. Impact Analysis
7. Remediation Steps
8. Prevention Recommendations
9. Confidence Score
"""

        response = self.llm.invoke(prompt)

        state["final_report"] = response.content

        state["confidence_score"] = 0.75

        return state