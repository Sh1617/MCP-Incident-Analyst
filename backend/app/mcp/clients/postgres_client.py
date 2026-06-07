import psycopg

from backend.app.core.database_config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)


class PostgresMCPClient:

    def __init__(self):

        self.connection_string = (
            f"host={POSTGRES_HOST} "
            f"port={POSTGRES_PORT} "
            f"dbname={POSTGRES_DB} "
            f"user={POSTGRES_USER} "
            f"password={POSTGRES_PASSWORD}"
        )

    def get_connection(self):

        return psycopg.connect(
            self.connection_string
        )

    async def get_incident_history(
        self,
        incident_id: str
    ):

        with self.get_connection() as conn:

            with conn.cursor() as cur:

                cur.execute(
                    """
                    SELECT
                        incident_id,
                        title,
                        description,
                        status
                    FROM incidents
                    WHERE incident_id = %s
                    """,
                    (incident_id,)
                )

                rows = cur.fetchall()

        return rows

    async def execute(
        self,
        query,
        params=None
    ):

        with self.get_connection() as conn:

            with conn.cursor() as cur:

                cur.execute(
                    query,
                    params
                )

            conn.commit()

        return True