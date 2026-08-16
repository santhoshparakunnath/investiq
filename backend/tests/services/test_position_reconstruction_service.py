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


def make_corporate_action(
    action_date,
    action_type,
    source_symbol,
    target_symbol=None,
    ratio_from=None,
    ratio_to=None,
):
    return SimpleNamespace(
        action_date=action_date,
        action_type=action_type,
        source_symbol=source_symbol,
        target_symbol=target_symbol,
        ratio_from=ratio_from,
        ratio_to=ratio_to,
        cost_allocation_percentage=None,
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

    corporate_action = make_corporate_action(
        action_date=date(2022, 7, 28),
        action_type=CorporateActionType.SPLIT,
        source_symbol="TATSTE",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("10"),
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

    corporate_action = make_corporate_action(
        action_date=date(2025, 8, 26),
        action_type=CorporateActionType.BONUS,
        source_symbol="HDFBAN",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("2"),
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

    corporate_action = make_corporate_action(
        action_date=date(2025, 6, 19),
        action_type=CorporateActionType.DEMERGER,
        source_symbol="SIEMEN",
        target_symbol="SIEENE",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("1"),
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["SIEMEN"] == Decimal("50")
    assert result["SIEENE"] == Decimal("50")


def test_merger_converts_source_into_target():
    transactions = [
        make_transaction(
            "STABTR",
            TransactionType.BUY,
            10,
            date(2017, 3, 1),
        ),
    ]

    corporate_action = make_corporate_action(
        action_date=date(2017, 4, 1),
        action_type=CorporateActionType.MERGER,
        source_symbol="STABTR",
        target_symbol="STABAN",
        ratio_from=Decimal("10"),
        ratio_to=Decimal("22"),
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["STABTR"] == Decimal("0")
    assert result["STABAN"] == Decimal("22")


def test_allotment_adds_shares_without_trade():
    corporate_action = make_corporate_action(
        action_date=date(2020, 1, 1),
        action_type=CorporateActionType.ALLOTMENT,
        source_symbol="VGUARD",
        ratio_to=Decimal("287"),
    )

    result = PositionReconstructionService().reconstruct(
        [],
        [corporate_action],
    )

    assert result["VGUARD"] == Decimal("287")


def test_extinguishment_removes_position():
    transactions = [
        make_transaction(
            "YESBAN",
            TransactionType.BUY,
            560,
            date(2020, 1, 1),
        ),
    ]

    corporate_action = make_corporate_action(
        action_date=date(2021, 1, 1),
        action_type=CorporateActionType.EXTINGUISHMENT,
        source_symbol="YESBAN",
    )

    result = PositionReconstructionService().reconstruct(
        transactions,
        [corporate_action],
    )

    assert result["YESBAN"] == Decimal("0")

def test_negative_position_indicates_opening_history_gap():
    transactions = [
        make_transaction(
            "RELIND",
            TransactionType.SELL,
            100,
            date(2013, 1, 7),
        ),
    ]

    result = PositionReconstructionService().reconstruct(transactions)

    assert result["RELIND"] == Decimal("-100")