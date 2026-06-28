from fastapi import APIRouter

from coordinator.api.health import router as health_router

api_router = APIRouter(prefix="/coordinator/api/v1")

api_router.include_router(health_router)
