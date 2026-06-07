from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager
from backend.app.core.metrics import AgentTimer


class LogAgent(BaseAgent):

    name = "log_agent"

    async def execute(self, state):

        timer = AgentTimer()
        timer.start()

        logs = await mcp_manager.filesystem.search_logs()

        findings = []

        for log_file in logs:

            content = await mcp_manager.filesystem.read_file(
                log_file
            )

            if content["status"] == "success":

                text = content["content"]

                errors = []

                for line in text.splitlines():

                    if "ERROR" in line:
                        errors.append(line)

                findings.append(
                    {
                        "file": log_file,
                        "error_detected": len(errors) > 0,
                        "error_count": len(errors),
                        "errors": errors
                    }
                )

        state["logs"] = findings

        state["findings"].append(
            {
                "agent": self.name,
                "results": findings
            }
        )

        if "agent_metrics" not in state:
            state["agent_metrics"] = {}

        state["agent_metrics"][
            self.name
        ] = timer.stop()

        return state