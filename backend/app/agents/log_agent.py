from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager


class LogAgent(BaseAgent):

    name = "log_agent"

    async def execute(self, state):

        logs = await mcp_manager.filesystem.search_logs()

        findings = []

        for log_file in logs:

            content = await mcp_manager.filesystem.read_file(
                log_file
            )

            if content["status"] == "success":

                text = content["content"]

                if "ERROR" in text:

                    findings.append(
                        {
                            "file": log_file,
                            "error_detected": True
                        }
                    )

        state["logs"] = findings

        state["findings"].append(
            {
                "agent": self.name,
                "results": findings
            }
        )

        return state