from decimal import Decimal

from app.models.corporate_action import (
    CorporateAction,
    CorporateActionType,
)
from app.services.position_adjustment_service import (
    PositionAdjustmentService,
)


def test_split_adjusts_quantity():

    action = CorporateAction(
        action_date=None,
        action_type=CorporateActionType.SPLIT,
        source_symbol="TEST",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("5"),
    )

    service = PositionAdjustmentService()

    result = service.adjust_quantity(
        Decimal("100"),
        action,
    )

    assert result == Decimal("500")


def test_bonus_adjusts_quantity():

    action = CorporateAction(
        action_date=None,
        action_type=CorporateActionType.BONUS,
        source_symbol="TEST",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("2"),
    )

    service = PositionAdjustmentService()

    result = service.adjust_quantity(
        Decimal("100"),
        action,
    )

    assert result == Decimal("200")


def test_demerger_does_not_change_quantity():

    action = CorporateAction(
        action_date=None,
        action_type=CorporateActionType.DEMERGER,
        source_symbol="TEST",
        target_symbol="NEW",
        ratio_from=Decimal("1"),
        ratio_to=Decimal("1"),
    )

    service = PositionAdjustmentService()

    result = service.adjust_quantity(
        Decimal("100"),
        action,
    )

    assert result == Decimal("100")


def test_missing_ratio_raises_error():

    action = CorporateAction(
        action_date=None,
        action_type=CorporateActionType.SPLIT,
        source_symbol="TEST",
        ratio_from=None,
        ratio_to=None,
    )

    service = PositionAdjustmentService()

    try:
        service.adjust_quantity(
            Decimal("100"),
            action,
        )
        assert False
    except ValueError as error:
        assert "requires a ratio" in str(error)