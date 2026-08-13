from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from app.models.corporate_action import CorporateActionType
from app.models.enums import TransactionType
from app.services.position_reconstruction_service import (
    PositionReconstructionService,
)


def make_transaction(symbol, action, quantity, trade_date):
    return SimpleNamespace(
        symbol=symbol,
        action=action,
        quantity=Decimal(quantity),
        trade_date=trade_date,
    )


def test_buy_increases_position():
    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            100,
            date(2021, 4, 6),
        )
    ]

    result = PositionReconstructionService().reconstruct(transactions)

    assert result["TATSTE"] == Decimal("100")


def test_sell_reduces_position():
    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            100,
            date(2021, 4, 6),
        ),
        make_transaction(
            "TATSTE",
            TransactionType.SELL,
            40,
            date(2022, 4, 6),
        ),
    ]

    result = PositionReconstructionService().reconstruct(transactions)

    assert result["TATSTE"] == Decimal("60")


def test_multiple_symbols_are_reconstructed_independently():
    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            100,
            date(2021, 4, 6),
        ),
        make_transaction(
            "HDFBAN",
            TransactionType.BUY,
            50,
            date(2021, 5, 6),
        ),
    ]

    result = PositionReconstructionService().reconstruct(transactions)

    assert result["TATSTE"] == Decimal("100")
    assert result["HDFBAN"] == Decimal("50")


def test_transactions_are_processed_chronologically():
    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.SELL,
            40,
            date(2022, 4, 6),
        ),
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            100,
            date(2021, 4, 6),
        ),
    ]

    result = PositionReconstructionService().reconstruct(transactions)

    assert result["TATSTE"] == Decimal("60")


def test_tatste_split_reconciles_position():
    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            120,
            date(2021, 4, 6),
        ),
        make_transaction(
            "TATSTE",
            TransactionType.SELL,
            1200,
            date(2025, 5, 23),
        ),
    ]

    corporate_action = SimpleNamespace(
        action_date=date(2022, 7, 28),
        action_type=CorporateActionType.SPLIT,
        source_symbol="TATSTE",
        target_symbol=None,
        ratio_from=Decimal("1"),
        ratio_to=Decimal("10"),
        cost_allocation_percentage=None,
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["TATSTE"] == Decimal("0")


def test_hdfban_bonus_doubles_position():
    transactions = [
        make_transaction(
            "HDFBAN",
            TransactionType.BUY,
            100,
            date(2024, 1, 4),
        ),
    ]

    corporate_action = SimpleNamespace(
        action_date=date(2025, 8, 26),
        action_type=CorporateActionType.BONUS,
        source_symbol="HDFBAN",
        target_symbol=None,
        ratio_from=Decimal("1"),
        ratio_to=Decimal("2"),
        cost_allocation_percentage=None,
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["HDFBAN"] == Decimal("200")


def test_siemen_demerger_creates_new_position():
    transactions = [
        make_transaction(
            "SIEMEN",
            TransactionType.BUY,
            50,
            date(2024, 1, 10),
        ),
    ]

    corporate_action = SimpleNamespace(
        action_date=date(2025, 6, 19),
        action_type=CorporateActionType.DEMERGER,
        source_symbol="SIEMEN",
        target_symbol="SIEENE",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("1"),
        cost_allocation_percentage=None,
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["SIEMEN"] == Decimal("50")
    assert result["SIEENE"] == Decimal("50")