from decimal import Decimal

from app.models.reconciliation import (
    PositionReconciliation,
    ReconciliationStatus,
)


class ReconciliationService:
    """
    Compares calculated portfolio positions against actual holdings.
    """

    def reconcile(
        self,
        symbol: str,
        calculated_quantity: Decimal,
        actual_quantity: Decimal,
    ) -> PositionReconciliation:

        difference = calculated_quantity - actual_quantity

        if difference == Decimal("0"):
            status = ReconciliationStatus.RECONCILED
            explanation = "Calculated position matches current holding."

        else:
            status = ReconciliationStatus.UNEXPLAINED
            explanation = (
                "Calculated position does not match current holding."
            )

        return PositionReconciliation(
            symbol=symbol,
            calculated_quantity=calculated_quantity,
            actual_quantity=actual_quantity,
            difference=difference,
            status=status,
            explanation=explanation,
        )