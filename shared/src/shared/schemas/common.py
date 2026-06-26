from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ParticipantResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    transaction_id: UUID
    success: bool
    message: str | None = None
