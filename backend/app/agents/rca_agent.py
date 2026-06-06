from backend.app.agents.base_agent import BaseAgent


class RCAAgent(BaseAgent):

    name = "rca_agent"

    async def execute(self, state: dict):
        state["final_report"] = "Dummy RCA Report"
        print("RCA Agent Executed")
        return state