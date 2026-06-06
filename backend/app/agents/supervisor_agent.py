from backend.app.agents.base_agent import BaseAgent


class SupervisorAgent(BaseAgent):

    name = "supervisor_agent"

    async def execute(self, state: dict):
        print("Supervisor Agent Executed")
        return state