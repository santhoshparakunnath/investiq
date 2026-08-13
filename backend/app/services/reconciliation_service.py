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
    opening_position_required: bool = False,
    corporate_action_explains_difference: bool = False,     
    ) -> PositionReconciliation:

        difference = calculated_quantity - actual_quantity

        if difference == Decimal("0"):
            status = ReconciliationStatus.RECONCILED
            explanation = "Calculated position matches current holding."

        elif opening_position_required:
            status = ReconciliationStatus.OPENING_POSITION_REQUIRED
            explanation = "Historical transaction data does not fully explain the current holding."

        elif corporate_action_explains_difference:
            status = ReconciliationStatus.CORPORATE_ACTION
            explanation = ("The position difference is explained by a corporate action.")

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