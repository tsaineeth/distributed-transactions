from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RollbackRequest(BaseModel):
    """
    Sent by the coordinator to instruct a participant
    to rollback its prepared transaction.
    """

    model_config = ConfigDict(extra="forbid")

    transaction_id: UUID


class RollbackResponse(BaseModel):
    """
    Returned by a participant after rolling back
    its prepared transaction.
    """

    ...
