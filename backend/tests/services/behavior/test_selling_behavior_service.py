from datetime import date
from decimal import Decimal

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.services.behavior.selling_behavior_service import SellingBehaviorService


def create_transaction(
    trade_date,
    symbol,
    action,
    quantity,
    price,
):
    return Transaction(
        trade_date=trade_date,
        symbol=symbol,
        action=action,
        quantity=quantity,
        price=Decimal(str(price)),
        trade_value=Decimal(str(price)) * quantity,
        charges=Charges(),
        exchange="NSE",
    )


def test_selling_behavior():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
            "1000.00",
        ),
        create_transaction(
            date(2021, 1, 1),
            "INFY",
            TransactionType.SELL,
            40,
            "1200.00",
        ),
        create_transaction(
            date(2022, 1, 1),
            "INFY",
            TransactionType.SELL,
            60,
            "800.00",
        ),
    ]

    service = SellingBehaviorService()

    result = service.analyze(transactions)

    assert result.total_sell_transactions == 2
    assert result.profit_taking_count == 1
    assert result.loss_taking_count == 1
    assert result.partial_sale_count == 1
    assert result.complete_exit_count == 1