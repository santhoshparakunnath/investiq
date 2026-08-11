from decimal import Decimal

from app.models.completed_investment import CompletedInvestment
from app.models.performance_analysis import PerformanceAnalysis


class PerformanceService:
    """
    Analyzes the performance of completed investments.
    """

    def analyze(
        self,
        investments: list[CompletedInvestment],
    ) -> PerformanceAnalysis:

        winning_investments = 0
        losing_investments = 0

        total_profit = Decimal("0.00")
        total_loss = Decimal("0.00")

        for investment in investments:

            if investment.realized_profit > 0:
                winning_investments += 1
                total_profit += investment.realized_profit

            elif investment.realized_profit < 0:
                losing_investments += 1
                total_loss += investment.realized_profit

        return PerformanceAnalysis(
            completed_investments=len(investments),
            winning_investments=winning_investments,
            losing_investments=losing_investments,
            total_profit=total_profit,
            total_loss=total_loss,
        )