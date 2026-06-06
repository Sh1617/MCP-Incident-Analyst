from backend.app.agents.base_agent import BaseAgent


class LogAgent(BaseAgent):

    name = "log_agent"

    async def execute(self, state: dict):
        print("Log Agent Executed")
        return state