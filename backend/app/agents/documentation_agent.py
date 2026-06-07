from backend.app.agents.base_agent import BaseAgent

from backend.app.vectorstore.retriever import (
    search_runbooks
)
from backend.app.core.tracing import tracer

class DocumentationAgent(BaseAgent):

    name = "documentation_agent"

    async def execute(self, state):

        with tracer.start_as_current_span(
            "documentation_agent_execution"
        ):

            docs = search_runbooks(
                state["user_query"]
            )

            state["documentation_results"] = docs

            state["findings"].append(
                {
                    "agent": self.name,
                    "results": docs
                }
            )

            return state