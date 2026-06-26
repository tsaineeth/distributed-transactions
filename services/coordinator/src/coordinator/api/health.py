from fastapi import APIRouter

from coordinator.config import get_settings
from coordinator.schemas.health import HealthResponse, ServiceInfoResponse

router = APIRouter(tags=["Health"])


@router.get("/", response_model=ServiceInfoResponse)
async def root() -> ServiceInfoResponse:
    settings = get_settings()

    return ServiceInfoResponse(
        service=settings.service_name,
        version=settings.version,
    )


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    settings = get_settings()

    return HealthResponse(
        status="healthy",
        service=settings.service_name,
        version=settings.version,
    )