from decimal import Decimal

from app.models.reconciliation import ReconciliationStatus
from app.services.reconciliation_service import ReconciliationService


def test_matching_position_is_reconciled():

    service = ReconciliationService()

    result = service.reconcile(
        symbol="ADAENT",
        calculated_quantity=Decimal("60"),
        actual_quantity=Decimal("60"),
    )

    assert result.difference == Decimal("0")
    assert result.status == ReconciliationStatus.RECONCILED


def test_different_position_is_unexplained():

    service = ReconciliationService()

    result = service.reconcile(
        symbol="ICIBAN",
        calculated_quantity=Decimal("960"),
        actual_quantity=Decimal("700"),
    )

    assert result.difference == Decimal("260")
    assert result.status == ReconciliationStatus.UNEXPLAINED


def test_difference_is_calculated_correctly():

    service = ReconciliationService()

    result = service.reconcile(
        symbol="HDFBAN",
        calculated_quantity=Decimal("565"),
        actual_quantity=Decimal("880"),
    )

    assert result.difference == Decimal("-315")