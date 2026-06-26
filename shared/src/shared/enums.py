from enum import StrEnum

from shared.database import Base


class TransactionState(StrEnum):
    STARTED = "STARTED"

    PREPARING = "PREPARING"
    PREPARED = "PREPARED"

    COMMITTING = "COMMITTING"
    COMMITTED = "COMMITTED"

    ROLLING_BACK = "ROLLING_BACK"
    ROLLED_BACK = "ROLLED_BACK"

    FAILED = "FAILED"
