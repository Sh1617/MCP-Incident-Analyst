from langgraph.graph import StateGraph
from langgraph.graph import END

from backend.app.graphs.state import IncidentState

from backend.app.agents.supervisor_agent import SupervisorAgent
from backend.app.agents.log_agent import LogAgent
from backend.app.agents.database_agent import DatabaseAgent
from backend.app.agents.github_agent import GitHubAgent
from backend.app.agents.documentation_agent import DocumentationAgent
from backend.app.agents.rca_agent import RCAAgent


supervisor = SupervisorAgent()
log_agent = LogAgent()
database_agent = DatabaseAgent()
github_agent = GitHubAgent()
documentation_agent = DocumentationAgent()
rca_agent = RCAAgent()


async def supervisor_node(state):
    return await supervisor.execute(state)


async def log_node(state):
    return await log_agent.execute(state)


async def database_node(state):
    return await database_agent.execute(state)


async def github_node(state):
    return await github_agent.execute(state)


async def documentation_node(state):
    return await documentation_agent.execute(state)


async def rca_node(state):
    return await rca_agent.execute(state)


graph = StateGraph(IncidentState)

graph.add_node("supervisor", supervisor_node)
graph.add_node("log_agent", log_node)
graph.add_node("database_agent", database_node)
graph.add_node("github_agent", github_node)
graph.add_node("documentation_agent", documentation_node)
graph.add_node("rca_agent", rca_node)

graph.set_entry_point("supervisor")

graph.add_edge("supervisor", "log_agent")
graph.add_edge("log_agent", "database_agent")
graph.add_edge("database_agent", "github_agent")
graph.add_edge("github_agent", "documentation_agent")
graph.add_edge("documentation_agent", "rca_agent")

graph.add_edge("rca_agent", END)

incident_graph = graph.compile()