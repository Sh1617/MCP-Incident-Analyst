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

        report_id = str(uuid4())

        await (
            mcp_manager.postgres.execute(
                query,
                (
                    report_id,
                    1,
                    report[:5000],
                    confidence_score
                )
            )
        )

        return report_id

    async def get_report(
        self,
        report_id
    ):

        query = """
        SELECT
            report_id,
            investigation_id,
            executive_summary,
            confidence_score,
            created_at
        FROM reports
        WHERE report_id = %s
        """

        with (
            mcp_manager.postgres.get_connection()
            as conn
        ):

            with conn.cursor() as cur:

                cur.execute(
                    query,
                    (report_id,)
                )

                row = cur.fetchone()

        if not row:
            return None

        return {
            "report_id": row[0],
            "investigation_id": row[1],
            "executive_summary": row[2],
            "confidence_score": row[3],
            "created_at": str(row[4])
        }