from uuid import UUID, uuid4

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from shared.database import Base, TimestampMixin
from shared.enums import TransactionState


class Transaction(TimestampMixin, Base):
    """
    Represents a distributed transaction managed by the coordinator.
    """

    __tablename__ = "transactions"

    transaction_id: Mapped[UUID] = mapped_column(
        unique=True,
        nullable=False,
        default=uuid4,
        index=True,
    )

    state: Mapped[TransactionState] = mapped_column(
        Enum(TransactionState, name="transaction_state"),
        nullable=False,
        default=TransactionState.STARTED,
    )
