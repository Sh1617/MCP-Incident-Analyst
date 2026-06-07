from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager
from backend.app.core.metrics import AgentTimer
from backend.app.core.logger import get_logger
from backend.app.core.tracing import tracer
from backend.app.api.metrics import (
    agent_metrics
)

logger = get_logger(__name__)


class LogAgent(BaseAgent):

    name = "log_agent"

    async def execute(self, state):

        with tracer.start_as_current_span(
            "log_agent_execution"
        ):

        # existing code here

            timer = AgentTimer()
            timer.start()

            logger.info(
                "Log Agent Started"
            )

            logs = await (
                mcp_manager.filesystem.search_logs()
            )

            findings = []

            for log_file in logs:

                content = await (
                    mcp_manager.filesystem.read_file(
                        log_file
                    )
                )

                if content["status"] == "success":

                    text = content["content"]

                    errors = []

                    for line in text.splitlines():

                        keywords = [
                            "ERROR",
                            "CRITICAL",
                            "EXCEPTION",
                            "TIMEOUT",
                            "FAILED"
                        ]

                        if any(
                            keyword in line.upper()
                            for keyword in keywords
                        ):

                            errors.append(
                                line
                            )

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

            logger.info(
                f"Log Agent Finished | "
                f"Files Processed={len(findings)} | "
                f"Execution Time={state['agent_metrics'][self.name]}s"
            )

            agent_metrics.update(
                state.get(
                    "agent_metrics",
                    {}
                )
            )

            return state