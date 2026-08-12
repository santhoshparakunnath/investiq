from decimal import Decimal

from app.models.reconciliation import (
    PositionReconciliation,
    ReconciliationStatus,
)


def test_reconciled_position():

    result = PositionReconciliation(
        symbol="ADAENT",
        calculated_quantity=Decimal("60"),
        actual_quantity=Decimal("60"),
        difference=Decimal("0"),
        status=ReconciliationStatus.RECONCILED,
    )

    assert result.symbol == "ADAENT"
    assert result.difference == Decimal("0")
    assert result.status == ReconciliationStatus.RECONCILED


def test_opening_position_required():

    result = PositionReconciliation(
        symbol="RELIND",
        calculated_quantity=Decimal("38"),
        actual_quantity=Decimal("712"),
        difference=Decimal("-674"),
        status=ReconciliationStatus.OPENING_POSITION_REQUIRED,
        explanation="Historical position predates available transaction history.",
    )

    assert result.status == ReconciliationStatus.OPENING_POSITION_REQUIRED
    assert result.explanation is not None