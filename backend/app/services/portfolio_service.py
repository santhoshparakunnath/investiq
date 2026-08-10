from decimal import Decimal
from app.models.holding import Holding
from app.models.portfolio_summary import PortfolioSummary


class PortfolioService:
    """
    Calculates portfolio information from holdings.
    """

    def get_summary(
        self,
        holdings: list[Holding]
    ) -> PortfolioSummary:

        total_value = sum(
            (holding.market_value for holding in holdings),
            Decimal("0.00")
        )

        holding_count = len(holdings)

        return PortfolioSummary(
            total_value=total_value,
            holding_count=holding_count,
        )