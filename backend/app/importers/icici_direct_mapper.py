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
            trade_date=datetime.strptime(
                str(row[DATE]),
                "%d-%b-%Y"
            ).date(),

            symbol=str(row[STOCK]).strip(),

            action=action,

            quantity=int(row[QUANTITY]),

            price=Decimal(str(row[PRICE])),

            trade_value=Decimal(str(row[TRADE_VALUE])),

            charges=charges,

            exchange=str(row[EXCHANGE]),

            order_number=str(row[ORDER_REF]),
        )