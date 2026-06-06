import asyncio

from backend.app.agents.database_agent import (
    DatabaseAgent
)


async def main():

    state = {
        "incident_id": "INC-001",
        "db_results": [],
        "findings": []
    }

    agent = DatabaseAgent()

    result = await agent.execute(
        state
    )

    print(result)


asyncio.run(main())