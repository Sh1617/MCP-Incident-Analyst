from backend.app.agents.base_agent import BaseAgent
from backend.app.llm.factory import LLMFactory


class RCAAgent(BaseAgent):

    name = "rca_agent"

    def __init__(self):
        self.llm = LLMFactory.get_llm()

    async def execute(self, state):

        prompt = f"""
You are an SRE Root Cause Analysis Agent.

User Query:
{state['user_query']}

Evidence:
{state['findings']}

Generate:

1. Executive Summary
2. Root Cause
3. Impact
4. Remediation Steps
"""

        response = self.llm.invoke(prompt)

        state["final_report"] = response.content

        state["confidence_score"] = 0.75

        return state