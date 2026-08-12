from datetime import datetime
from decimal import Decimal

from app.importers.icici_columns import (
    ACTION,
    BROKERAGE,
    DATE,
    EXCHANGE,
    ORDER_REF,
    PRICE,
    QUANTITY,
    STOCK,
    STAMP_DUTY,
    STT,
    TRADE_VALUE,
    TRANSACTION_AND_SEBI,
)

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction


class ICICIDirectMapper:
    """
    Maps one ICICI Direct tradebook row into a Transaction.
    """

    def to_transaction(self, row) -> Transaction:

        # ICICI exports may use different date formats.
        date_value = str(row[DATE]).strip()

        trade_date = None

        for date_format in ("%d-%b-%Y", "%d-%m-%Y", "%d-%b-%y"):
            try:
                trade_date = datetime.strptime(
                    date_value,
                    date_format
                ).date()
                break
            except ValueError:
                continue

        if trade_date is None:
            raise ValueError(f"Invalid trade date: {date_value}")

        action = (
            TransactionType.BUY
            if str(row[ACTION]).strip().lower() == "buy"
            else TransactionType.SELL
        )

        charges = Charges(
            brokerage=Decimal(str(row[BROKERAGE])),
            stt=Decimal(str(row[STT])),
            stamp_duty=Decimal(str(row[STAMP_DUTY])),
            transaction_and_sebi_charges=Decimal(
                str(row[TRANSACTION_AND_SEBI])
            ),
        )

        return Transaction(
            trade_date=trade_date,
            symbol=str(row[STOCK]).strip(),
            action=action,
            quantity=int(row[QUANTITY]),
            price=Decimal(str(row[PRICE])),
            trade_value=Decimal(str(row[TRADE_VALUE])),
            charges=charges,
            exchange=str(row[EXCHANGE]).strip(),
            order_number=str(row[ORDER_REF]).strip(),
        )