from collections import defaultdict
from decimal import Decimal

from app.models.enums import TransactionType


class PositionReconstructionService:
    """
    Reconstructs share quantities from BUY and SELL transactions.

    Corporate actions will be added in a later step.
    """

    def reconstruct(self, transactions) -> dict[str, Decimal]:
        positions = defaultdict(Decimal)

        for transaction in sorted(
            transactions,
            key=lambda transaction: transaction.trade_date,
        ):
            if transaction.action == TransactionType.BUY:
                positions[transaction.symbol] += Decimal(
                    transaction.quantity
                )

            elif transaction.action == TransactionType.SELL:
                positions[transaction.symbol] -= Decimal(
                    transaction.quantity
                )

        return dict(positions)