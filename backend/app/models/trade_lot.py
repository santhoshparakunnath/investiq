from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class TradeLot:
    """
    Represents one buy lot that may be partially or fully sold.
    """

    trade_date: date

    quantity: int

    price: Decimal