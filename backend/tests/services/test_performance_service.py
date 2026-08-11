from datetime import date
from decimal import Decimal

from app.models.completed_investment import CompletedInvestment
from app.services.performance_service import PerformanceService


def test_performance_analysis():

    investments = [
        CompletedInvestment(
            symbol="INFY",
            first_buy_date=date(2020, 1, 1),
            final_sell_date=date(2022, 1, 1),
            holding_days=731,
            total_quantity=100,
            total_cost=Decimal("100000.00"),
            total_sale_value=Decimal("150000.00"),
            realized_profit=Decimal("50000.00"),
        ),
        CompletedInvestment(
            symbol="TCS",
            first_buy_date=date(2020, 1, 1),
            final_sell_date=date(2021, 1, 1),
            holding_days=366,
            total_quantity=50,
            total_cost=Decimal("100000.00"),
            total_sale_value=Decimal("80000.00"),
            realized_profit=Decimal("-20000.00"),
        ),
    ]

    service = PerformanceService()

    result = service.analyze(investments)

    assert result.completed_investments == 2
    assert result.winning_investments == 1
    assert result.losing_investments == 1
    assert result.total_profit == Decimal("50000.00")
    assert result.total_loss == Decimal("-20000.00")