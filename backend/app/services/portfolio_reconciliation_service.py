from decimal import Decimal

from app.services.position_reconstruction_service import (
    PositionReconstructionService,
)
from app.services.reconciliation_service import ReconciliationService


class PortfolioReconciliationService:

    def __init__(self):
        self.position_reconstruction_service = PositionReconstructionService()
        self.reconciliation_service = ReconciliationService()

    def reconcile(
        self,
        transactions,
        holdings,
        corporate_actions=None,
    ):

        corporate_actions = corporate_actions or []

        calculated_positions = (
            self.position_reconstruction_service.reconstruct(
                transactions,
                corporate_actions,
            )
        )

        actual_positions = {
            holding.symbol: Decimal(str(holding.quantity))
            for holding in holdings
        }

        symbols = set(calculated_positions) | set(actual_positions)

        results = []

        for symbol in sorted(symbols):

            calculated_quantity = calculated_positions.get(
                symbol,
                Decimal("0"),
            )

            actual_quantity = actual_positions.get(
                symbol,
                Decimal("0"),
            )

            result = self.reconciliation_service.reconcile(
                symbol=symbol,
                calculated_quantity=calculated_quantity,
                actual_quantity=actual_quantity,
            )

            results.append(result)

        return results