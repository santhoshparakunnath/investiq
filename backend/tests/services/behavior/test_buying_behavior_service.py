from datetime import date
from decimal import Decimal

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.services.behavior.buying_behavior_service import BuyingBehaviorService


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


def test_buying_behavior():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
            "1000.00",
        ),
        create_transaction(
            date(2020, 6, 1),
            "INFY",
            TransactionType.BUY,
            50,
            "800.00",
        ),
        create_transaction(
            date(2021, 1, 1),
            "INFY",
            TransactionType.BUY,
            50,
            "900.00",
        ),
        create_transaction(
            date(2021, 6, 1),
            "INFY",
            TransactionType.BUY,
            50,
            "900.00",
        ),
    ]

    service = BuyingBehaviorService()

    result = service.analyze(transactions)

    assert result.total_buy_transactions == 4
    assert result.repeat_purchase_count == 3
    assert result.averaging_down_count == 1
    assert result.averaging_up_count == 1
    assert result.same_price_count == 1