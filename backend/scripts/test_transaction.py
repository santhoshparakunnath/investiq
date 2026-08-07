import sys
from pathlib import Path
from datetime import date
from decimal import Decimal

# Add the backend folder to Python's import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.models.transaction import Transaction
from app.models.enums import TransactionType


transaction = Transaction(
    trade_date=date(2024, 4, 1),
    symbol="INFY",
    action=TransactionType.BUY,
    quantity=10,
    price=Decimal("1500.25"),
    trade_value=Decimal("15002.50"),
    brokerage=Decimal("20.00"),
    taxes=Decimal("5.50"),
    exchange="NSE",
)

print(transaction)