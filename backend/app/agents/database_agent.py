from backend.app.agents.base_agent import BaseAgent


class DatabaseAgent(BaseAgent):

    name = "database_agent"

    async def execute(self, state: dict):
        print("Database Agent Executed")
        return state