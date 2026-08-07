import sys
from pathlib import Path
from datetime import date
from decimal import Decimal

# Add backend folder to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction


charges = Charges(
    brokerage=Decimal("20.00"),
    gst=Decimal("3.60"),
    stt=Decimal("15.20"),
)

transaction = Transaction(
    trade_date=date(2024, 4, 1),
    symbol="INFY",
    action=TransactionType.BUY,
    quantity=10,
    price=Decimal("1500.25"),
    trade_value=Decimal("15002.50"),
    charges=charges,
    exchange="NSE",
)

print(transaction)
print()
print(f"Total Charges : {transaction.charges.total}")