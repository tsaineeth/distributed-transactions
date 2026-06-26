from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from coordinator.api import api_router
from coordinator.config import get_settings
from shared.logging.logger import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """
    Manage application startup and shutdown.

    Future responsibilities:
    - Initialize RabbitMQ connections
    - Initialize database engine
    - Configure OpenTelemetry
    - Warm caches
    """

    configure_logging()
    settings = get_settings()

    print(f"Starting {settings.service_name}")

    yield

    print(f"Stopping {settings.service_name}")


def create_app() -> FastAPI:

    settings = get_settings()

    app = FastAPI(
        title=settings.service_name,
        version=settings.version,
        lifespan=lifespan,
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    app.include_router(api_router)

    return app
