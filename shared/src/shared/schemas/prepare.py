from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from shared.schemas.common import ParticipantResponse


class PrepareRequest(BaseModel):
    """
    Sent by the coordinator to ask a participant to prepare
    its local transaction.
    """

    model_config = ConfigDict(extra="forbid")

    transaction_id: UUID
    participant: str
    payload: dict[str, Any] = Field(default_factory=dict)


class PrepareResponse(ParticipantResponse):
    """
    Returned by a participant after executing the prepare phase.
    """

    ...
