from uuid import uuid4

from backend.app.mcp.manager import (
    mcp_manager
)


class InvestigationRepository:

    async def save_report(
        self,
        report,
        confidence_score
    ):

        query = """
        INSERT INTO reports
        (
            report_id,
            investigation_id,
            executive_summary,
            confidence_score
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """

        await (
            mcp_manager.postgres.execute(
                query,
                (
                    str(uuid4()),
                    1,
                    report[:5000],
                    confidence_score
                )
            )
        )

        return True