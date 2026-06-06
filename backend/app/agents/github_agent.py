from backend.app.agents.base_agent import BaseAgent


class GitHubAgent(BaseAgent):

    name = "github_agent"

    async def execute(self, state: dict):
        print("GitHub Agent Executed")
        return state