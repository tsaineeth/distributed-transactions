from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from shared.enums import TransactionState


class TransactionStatusResponse(BaseModel):
    """
    Response returned by the coordinator describing
    the current transaction state.
    """

    model_config = ConfigDict(from_attributes=True)

    transaction_id: UUID
    state: TransactionState
    created_at: datetime
    updated_at: datetime


class CreateTransactionResponse(BaseModel):
    """
    Response returned immediately after a transaction
    has been created.
    """

    transaction_id: UUID
    state: TransactionState = Field(default=TransactionState.STARTED)
