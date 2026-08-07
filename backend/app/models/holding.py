from dataclasses import dataclass, field
from decimal import Decimal

from app.models.trade_lot import TradeLot


@dataclass
class Holding:
    """
    Represents the current holding for a single stock.
    """

    symbol: str

    lots: list[TradeLot] = field(default_factory=list)

    market_price: Decimal = Decimal("0.00")