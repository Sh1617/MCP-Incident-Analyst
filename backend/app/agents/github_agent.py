from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager
from backend.app.core.metrics import AgentTimer
from backend.app.core.logger import get_logger
from backend.app.core.tracing import tracer

logger = get_logger(__name__)


class GitHubAgent(BaseAgent):

    name = "github_agent"

    async def execute(self, state):

        with tracer.start_as_current_span(
            "github_agent_execution"
        ):

            timer = AgentTimer()
            timer.start()

            logger.info(
                "GitHub Agent Started"
            )

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

            logger.info(
                f"GitHub Agent Finished | "
                f"Commits Found={len(commits)} | "
                f"Execution Time={state['agent_metrics'][self.name]}s"
            )

            return state