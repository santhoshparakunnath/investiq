from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class ReconciliationStatus(Enum):
    RECONCILED = "RECONCILED"
    CORPORATE_ACTION = "CORPORATE_ACTION"
    OPENING_POSITION_REQUIRED = "OPENING_POSITION_REQUIRED"
    UNEXPLAINED = "UNEXPLAINED"


@dataclass
class PositionReconciliation:
    symbol: str
    calculated_quantity: Decimal
    actual_quantity: Decimal
    difference: Decimal
    status: ReconciliationStatus
    explanation: str | None = None