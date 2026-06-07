from backend.app.agents.base_agent import BaseAgent
from backend.app.mcp.manager import mcp_manager
from backend.app.core.tracing import tracer

class DatabaseAgent(BaseAgent):

    name = "database_agent"

    async def execute(self, state):

        with tracer.start_as_current_span(
            "database_agent_execution"
        ):

            incident_id = state.get(
                "incident_id",
                "INC-001"
            )

            result = await (
                mcp_manager.postgres
                .get_incident_history(
                    incident_id
                )
            )

            state["db_results"] = result

            state["findings"].append(
                {
                    "agent": self.name,
                    "incident_history": result
                }
            )

            return state