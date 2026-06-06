from app.mcp.clients.postgres_client import PostgresMCPClient
from app.mcp.clients.github_client import GitHubMCPClient
from app.mcp.clients.filesystem_client import FilesystemMCPClient


class MCPManager:

    def __init__(self):
        self.postgres = PostgresMCPClient()
        self.github = GitHubMCPClient()
        self.filesystem = FilesystemMCPClient()


mcp_manager = MCPManager()