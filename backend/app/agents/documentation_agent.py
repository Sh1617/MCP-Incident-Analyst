from backend.app.agents.base_agent import BaseAgent


class DocumentationAgent(BaseAgent):

    name = "documentation_agent"

    async def execute(self, state: dict):
        print("Documentation Agent Executed")
        return state