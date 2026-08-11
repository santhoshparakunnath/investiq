from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class CompletedInvestment:
    """
    Represents one completed investment lifecycle.
    """

    symbol: str

    first_buy_date: date

    final_sell_date: date

    holding_days: int

    total_quantity: int

    total_cost: Decimal

    total_sale_value: Decimal

    realized_profit: Decimal