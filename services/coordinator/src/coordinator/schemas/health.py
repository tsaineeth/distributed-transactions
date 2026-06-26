from pydantic import BaseModel


class ServiceInfoResponse(BaseModel):
    service: str
    version: str


class HealthResponse(ServiceInfoResponse):
    status: str