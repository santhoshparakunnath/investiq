from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class CorporateActionType(Enum):
    SPLIT = "SPLIT"
    BONUS = "BONUS"
    DEMERGER = "DEMERGER"
    MERGER = "MERGER"
    SYMBOL_CHANGE = "SYMBOL_CHANGE"
    ISIN_CHANGE = "ISIN_CHANGE"


@dataclass
class CorporateAction:
    """
    Represents a corporate action that changes an investment
    position without being a normal BUY or SELL transaction.
    """

    action_date: date

    action_type: CorporateActionType

    source_symbol: str

    target_symbol: str | None = None

    ratio_from: Decimal | None = None

    ratio_to: Decimal | None = None

    cost_allocation_percentage: Decimal | None = None