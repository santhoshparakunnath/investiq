from dataclasses import dataclass
from datetime import date


@dataclass
class ImportSummary:
    """
    Summary of a completed import.
    """

    broker: str

    transaction_count: int

    first_trade_date: date | None

    last_trade_date: date | None