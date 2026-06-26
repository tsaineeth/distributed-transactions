from uuid import UUID

from pydantic import BaseModel, ConfigDict

from shared.schemas.common import ParticipantResponse


class CommitRequest(BaseModel):
    """
    Sent by the coordinator to instruct a participant
    to commit its prepared transaction.
    """

    model_config = ConfigDict(extra="forbid")

    transaction_id: UUID


class CommitResponse(ParticipantResponse):
    """
    Returned by a participant after committing
    its prepared transaction.
    """

    ...
