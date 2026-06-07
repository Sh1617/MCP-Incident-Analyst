import asyncio

from backend.app.mcp.clients.github_client import (
    GitHubMCPClient
)


async def main():

    client = GitHubMCPClient()

    commits = await client.search_recent_commits()

    print(commits)


asyncio.run(main())