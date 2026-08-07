from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional
from app.models.enums import TransactionType


@dataclass
class Transaction:
    """
    Represents a single stock market transaction.
    """

    trade_date: date
    symbol: str
    # action: str          # BUY or SELL


    action: TransactionType

    quantity: int

    price: Decimal

    trade_value: Decimal

    brokerage: Decimal

    taxes: Decimal

    exchange: str

    order_number: Optional[str] = None

    isin: Optional[str] = None