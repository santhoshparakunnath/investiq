from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PortfolioSummary:
    """
    Summary of the current portfolio.
    """

    total_value: Decimal
    holding_count: int