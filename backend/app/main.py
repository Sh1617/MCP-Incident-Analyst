from fastapi import FastAPI

from backend.app.api.health import (
    router as health_router
)

from backend.app.api.investigate import (
    router as investigate_router
)

from backend.app.api.routes.reports import (
    router as reports_router
)

from backend.app.core.config import settings
from backend.app.core.logging import setup_logging

from backend.app.api.investigations import (
    router as investigations_router
)
from backend.app.api.metrics import (
    router as metrics_router
)

logger = setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="AI-Powered Incident Investigation Platform"
)

# Routers
app.include_router(
    health_router
)

app.include_router(
    investigate_router
)

app.include_router(
    reports_router
)

app.include_router(
    investigations_router
)

app.include_router(
    metrics_router
)


@app.on_event("startup")
async def startup_event():

    logger.info(
        "MCP Incident Analyst started"
    )


@app.get("/")
async def root():

    return {
        "application": settings.APP_NAME,
        "environment": settings.ENVIRONMENT,
        "status": "running"
    }