from dataclasses import dataclass, field
from decimal import Decimal

from app.models.trade_lot import TradeLot


@dataclass
class Holding:
    """
    Represents the current holding for a single stock.
    """

    symbol: str
    stock_name: str
    isin: str

    quantity: int

    market_price: Decimal = Decimal("0.00")
    market_value: Decimal = Decimal("0.00")

    lots: list[TradeLot] = field(default_factory=list)