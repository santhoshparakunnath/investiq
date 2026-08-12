import json
from datetime import date
from decimal import Decimal

from app.models.corporate_action import (
    CorporateAction,
    CorporateActionType,
)


class CorporateActionRepository:
    """
    Loads corporate actions from the configured JSON data source.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_all(self) -> list[CorporateAction]:
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            CorporateAction(
                action_date=date.fromisoformat(item["action_date"]),
                action_type=CorporateActionType(item["action_type"]),
                source_symbol=item["source_symbol"],
                target_symbol=item.get("target_symbol"),
                ratio_from=(
                    Decimal(item["ratio_from"])
                    if item.get("ratio_from") is not None
                    else None
                ),
                ratio_to=(
                    Decimal(item["ratio_to"])
                    if item.get("ratio_to") is not None
                    else None
                ),
                cost_allocation_percentage=(
                    Decimal(item["cost_allocation_percentage"])
                    if item.get("cost_allocation_percentage") is not None
                    else None
                ),
            )
            for item in data
        ]

    def get_for_symbol(
        self,
        symbol: str,
    ) -> list[CorporateAction]:

        return [
            action
            for action in self.get_all()
            if action.source_symbol == symbol
            or action.target_symbol == symbol
        ]