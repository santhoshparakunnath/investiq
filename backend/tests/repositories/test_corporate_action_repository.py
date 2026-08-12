from datetime import date
from decimal import Decimal

from app.models.corporate_action import CorporateActionType
from app.repositories.corporate_action_repository import (
    CorporateActionRepository,
)


CORPORATE_ACTION_FILE = "data/corporate_actions.json"


def test_loads_all_corporate_actions():

    repository = CorporateActionRepository(CORPORATE_ACTION_FILE)

    actions = repository.get_all()

    assert len(actions) == 13


def test_finds_actions_for_source_symbol():

    repository = CorporateActionRepository(CORPORATE_ACTION_FILE)

    actions = repository.get_for_symbol("RELIND")

    assert len(actions) == 3


def test_finds_demerger_using_target_symbol():

    repository = CorporateActionRepository(CORPORATE_ACTION_FILE)

    actions = repository.get_for_symbol("SIEENE")

    assert len(actions) == 1

    action = actions[0]

    assert action.action_type == CorporateActionType.DEMERGER
    assert action.source_symbol == "SIEMEN"
    assert action.target_symbol == "SIEENE"


def test_bonus_ratio_is_loaded_correctly():

    repository = CorporateActionRepository(CORPORATE_ACTION_FILE)

    actions = repository.get_for_symbol("HDFBAN")

    assert len(actions) == 1

    action = actions[0]

    assert action.action_type == CorporateActionType.BONUS
    assert action.action_date == date(2025, 8, 26)
    assert action.ratio_from == Decimal("1")
    assert action.ratio_to == Decimal("2")


def test_optional_fields_can_be_none():

    repository = CorporateActionRepository(CORPORATE_ACTION_FILE)

    actions = repository.get_for_symbol("HDFBAN")

    action = actions[0]

    assert action.target_symbol is None
    assert action.cost_allocation_percentage is None
    