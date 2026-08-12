from decimal import Decimal

from app.models.corporate_action import (
    CorporateAction,
    CorporateActionType,
)


class PositionAdjustmentService:
    """
    Applies quantity adjustments caused by splits and bonus issues.

    This service does not handle demergers yet.
    """

    def adjust_quantity(
        self,
        quantity: Decimal,
        corporate_action: CorporateAction,
    ) -> Decimal:

        if corporate_action.action_type not in (
            CorporateActionType.SPLIT,
            CorporateActionType.BONUS,
        ):
            return quantity

        if (
            corporate_action.ratio_from is None
            or corporate_action.ratio_to is None
        ):
            raise ValueError(
                "Split/bonus corporate action requires a ratio."
            )

        if corporate_action.ratio_from <= 0:
            raise ValueError(
                "Corporate action ratio_from must be greater than zero."
            )

        return (
            quantity
            * corporate_action.ratio_to
            / corporate_action.ratio_from
        )