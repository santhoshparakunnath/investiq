from collections import defaultdict
from decimal import Decimal

from app.models.enums import TransactionType


class PositionReconstructionService:

    def reconstruct(
        self,
        transactions,
        corporate_actions=None,
    ) -> dict[str, Decimal]:

        positions = defaultdict(Decimal)
        corporate_actions = corporate_actions or []

        events = []

        # Add transactions as events
        for transaction in transactions:
            events.append(
                (
                    transaction.trade_date,
                    "TRANSACTION",
                    transaction,
                )
            )

        # Add corporate actions as events
        for action in corporate_actions:
            events.append(
                (
                    action.action_date,
                    "CORPORATE_ACTION",
                    action,
                )
            )

        # Process everything chronologically
        events.sort(key=lambda event: event[0])

        for _, event_type, event in events:

            # -------------------------
            # Transaction
            # -------------------------
            if event_type == "TRANSACTION":

                if event.action == TransactionType.BUY:
                    positions[event.symbol] += Decimal(event.quantity)

                elif event.action == TransactionType.SELL:
                    positions[event.symbol] -= Decimal(event.quantity)

            # -------------------------
            # Corporate Action
            # -------------------------
            elif event_type == "CORPORATE_ACTION":

                action_type = event.action_type.value
                source_symbol = event.source_symbol

                # -------------------------
                # Split / Bonus
                # -------------------------
                if action_type in ["SPLIT", "BONUS"]:

                    if source_symbol in positions:
                        positions[source_symbol] = (
                            positions[source_symbol]
                            * event.ratio_to
                            / event.ratio_from
                        )

                # -------------------------
                # Demerger
                # -------------------------
                elif action_type == "DEMERGER":

                    if source_symbol in positions:

                        source_quantity = positions[source_symbol]

                        target_symbol = event.target_symbol

                        if target_symbol:
                            target_quantity = (
                                source_quantity
                                * event.ratio_to
                                / event.ratio_from
                            )

                            positions[target_symbol] += target_quantity

        return dict(positions)