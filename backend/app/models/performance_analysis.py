from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PerformanceAnalysis:
    """
    Summary of completed investment performance.
    """

    completed_investments: int
    winning_investments: int
    losing_investments: int
    total_profit: Decimal
    total_loss: Decimal