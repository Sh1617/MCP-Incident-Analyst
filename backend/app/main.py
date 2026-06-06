from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging

logger = setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="AI-Powered Incident Investigation Platform"
)

app.include_router(health_router)


@app.on_event("startup")
async def startup_event():
    logger.info("MCP Incident Analyst started")


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "environment": settings.ENVIRONMENT,
        "status": "running"
    }