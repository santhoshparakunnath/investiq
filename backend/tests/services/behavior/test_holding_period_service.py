from datetime import date
from decimal import Decimal

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.services.behavior.holding_period_service import HoldingPeriodService


def create_transaction(
    trade_date,
    symbol,
    action,
    quantity,
):
    return Transaction(
        trade_date=trade_date,
        symbol=symbol,
        action=action,
        quantity=quantity,
        price=Decimal("100.00"),
        trade_value=Decimal("10000.00"),
        charges=Charges(),
        exchange="NSE",
    )


def test_holding_period_for_completed_position():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
        ),
        create_transaction(
            date(2022, 1, 1),
            "INFY",
            TransactionType.SELL,
            100,
        ),
    ]

    service = HoldingPeriodService()

    result = service.analyze(transactions)

    assert result.completed_positions == 1
    assert result.average_days == 731
    assert result.longest_days == 731
    assert result.shortest_days == 731


def test_open_position_is_not_counted():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
        ),
    ]

    service = HoldingPeriodService()

    result = service.analyze(transactions)

    assert result.completed_positions == 0
    assert result.average_days == 0
    assert result.longest_days == 0
    assert result.shortest_days == 0


def test_partial_sale():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
        ),
        create_transaction(
            date(2022, 1, 1),
            "INFY",
            TransactionType.SELL,
            40,
        ),
    ]

    service = HoldingPeriodService()

    result = service.analyze(transactions)

    assert result.completed_positions == 1
    assert result.average_days == 731
    assert result.longest_days == 731
    assert result.shortest_days == 731