import asyncio

from backend.app.agents.log_agent import LogAgent


async def main():

    state = {
        "logs": [],
        "findings": []
    }

    agent = LogAgent()

    result = await agent.execute(state)

    print(result)


asyncio.run(main())