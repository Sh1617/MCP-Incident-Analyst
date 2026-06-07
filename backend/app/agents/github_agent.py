from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager
from backend.app.core.metrics import AgentTimer


class GitHubAgent(BaseAgent):

    name = "github_agent"

    async def execute(self, state):

        timer = AgentTimer()
        timer.start()

        print("GitHub Agent Started")

        commits = await (
            mcp_manager.github.search_recent_commits(
                limit=5
            )
        )

        state["github_results"] = commits

        state["findings"].append(
            {
                "agent": self.name,
                "recent_commits": commits
            }
        )

        if "agent_metrics" not in state:
            state["agent_metrics"] = {}

        state["agent_metrics"][
            self.name
        ] = timer.stop()

        print("GitHub Agent Executed")

        return state