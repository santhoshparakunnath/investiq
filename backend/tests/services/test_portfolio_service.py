from decimal import Decimal

from app.models.holding import Holding
from app.services.portfolio_service import PortfolioService


def test_get_summary():

    holdings = [
        Holding(
            symbol="INFY",
            stock_name="Infosys Ltd",
            isin="INE009A01021",
            quantity=100,
            market_price=Decimal("1500.00"),
            market_value=Decimal("150000.00"),
        ),
        Holding(
            symbol="TCS",
            stock_name="Tata Consultancy Services",
            isin="INE467B01029",
            quantity=50,
            market_price=Decimal("3500.00"),
            market_value=Decimal("175000.00"),
        ),
    ]

    service = PortfolioService()

    summary = service.get_summary(holdings)

    assert summary.total_value == Decimal("325000.00")
    assert summary.holding_count == 2

def test_get_summary_with_empty_portfolio():
    holdings = []

    service = PortfolioService()

    summary = service.get_summary(holdings)

    assert summary.total_value == Decimal("0.00")
    assert summary.holding_count == 0