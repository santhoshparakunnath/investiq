from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from app.models.enums import TransactionType
from app.services.position_reconstruction_service import (
    PositionReconstructionService,
)


def make_transaction(symbol, action, quantity, trade_date):
    return SimpleNamespace(
        symbol=symbol,
        action=action,
        quantity=quantity,
        trade_date=trade_date,
    )


def test_buy_increases_position():

    transactions = [
        make_transaction(
            "TEST",
            TransactionType.BUY,
            100,
            date(2025, 1, 1),
        )
    ]

    result = PositionReconstructionService().reconstruct(
        transactions
    )

    assert result["TEST"] == Decimal("100")


def test_sell_reduces_position():

    transactions = [
        make_transaction(
            "TEST",
            TransactionType.BUY,
            100,
            date(2025, 1, 1),
        ),
        make_transaction(
            "TEST",
            TransactionType.SELL,
            40,
            date(2025, 2, 1),
        ),
    ]

    result = PositionReconstructionService().reconstruct(
        transactions
    )

    assert result["TEST"] == Decimal("60")


def test_multiple_symbols_are_reconstructed_independently():

    transactions = [
        make_transaction(
            "AAA",
            TransactionType.BUY,
            100,
            date(2025, 1, 1),
        ),
        make_transaction(
            "BBB",
            TransactionType.BUY,
            200,
            date(2025, 1, 2),
        ),
        make_transaction(
            "AAA",
            TransactionType.SELL,
            25,
            date(2025, 1, 3),
        ),
    ]

    result = PositionReconstructionService().reconstruct(
        transactions
    )

    assert result["AAA"] == Decimal("75")
    assert result["BBB"] == Decimal("200")


def test_transactions_are_processed_chronologically():

    transactions = [
        make_transaction(
            "TEST",
            TransactionType.SELL,
            50,
            date(2025, 2, 1),
        ),
        make_transaction(
            "TEST",
            TransactionType.BUY,
            100,
            date(2025, 1, 1),
        ),
    ]

    result = PositionReconstructionService().reconstruct(
        transactions
    )

    assert result["TEST"] == Decimal("50")