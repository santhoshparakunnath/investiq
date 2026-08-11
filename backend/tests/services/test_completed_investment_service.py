from datetime import date
from decimal import Decimal

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.services.completed_investment_service import CompletedInvestmentService


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


def test_completed_investment_with_full_sale():

    transactions = [
        create_transaction(
            date(2020, 1, 1),
            "INFY",
            TransactionType.BUY,
            100,
            "1000.00",
        ),
        create_transaction(
            date(2022, 1, 1),
            "INFY",
            TransactionType.SELL,
            100,
            "1500.00",
        ),
    ]

    service = CompletedInvestmentService()

    result = service.build_completed_investments(transactions)

    assert len(result) == 1

    investment = result[0]

    assert investment.symbol == "INFY"
    assert investment.first_buy_date == date(2020, 1, 1)
    assert investment.final_sell_date == date(2022, 1, 1)
    assert investment.holding_days == 731
    assert investment.total_quantity == 100
    assert investment.total_cost == Decimal("100000.00")
    assert investment.total_sale_value == Decimal("150000.00")
    assert investment.realized_profit == Decimal("50000.00")
    assert investment.return_percentage == Decimal("50.00")


def test_partial_sales_create_one_completed_investment():

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
            "1500.00",
        ),
    ]

    service = CompletedInvestmentService()

    result = service.build_completed_investments(transactions)

    assert len(result) == 1

    investment = result[0]

    assert investment.symbol == "INFY"
    assert investment.total_quantity == 100
    assert investment.total_cost == Decimal("100000.00")
    assert investment.total_sale_value == Decimal("138000.00")
    assert investment.realized_profit == Decimal("38000.00")
    assert investment.return_percentage == Decimal("38.00")
    assert investment.final_sell_date == date(2022, 1, 1)


def test_open_position_is_not_completed():

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
    ]

    service = CompletedInvestmentService()

    result = service.build_completed_investments(transactions)

    assert len(result) == 0