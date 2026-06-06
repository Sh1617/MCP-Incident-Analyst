import asyncio

from backend.app.graphs.workflow import incident_graph


async def main():

    result = await incident_graph.ainvoke(
        {
            "user_query": "Why did payment service fail yesterday?",
            "incident_id": "INC-001",
            "logs": [],
            "github_results": [],
            "db_results": [],
            "documentation_results": [],
            "findings": [],
            "confidence_score": 0.0,
            "final_report": ""
        }
    )

    print(result["final_report"])


asyncio.run(main())