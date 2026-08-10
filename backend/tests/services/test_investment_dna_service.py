from datetime import date
from decimal import Decimal

from app.models.charges import Charges
from app.models.enums import TransactionType
from app.models.holding import Holding
from app.models.transaction import Transaction
from app.services.investment_dna_service import InvestmentDNAService


def test_build_investment_dna():

    transactions = [

        Transaction(
            trade_date=date(2020, 1, 1),
            symbol="INFY",
            action=TransactionType.BUY,
            quantity=100,
            price=Decimal("1000"),
            trade_value=Decimal("100000"),
            charges=Charges(),
            exchange="NSE",
            order_number="1",
        ),

        Transaction(
            trade_date=date(2020, 6, 1),
            symbol="INFY",
            action=TransactionType.SELL,
            quantity=50,
            price=Decimal("1200"),
            trade_value=Decimal("60000"),
            charges=Charges(),
            exchange="NSE",
            order_number="2",
        ),

        Transaction(
            trade_date=date(2021, 1, 1),
            symbol="TCS",
            action=TransactionType.BUY,
            quantity=25,
            price=Decimal("3000"),
            trade_value=Decimal("75000"),
            charges=Charges(),
            exchange="NSE",
            order_number="3",
        ),
    ]

    holdings = [

        Holding(
            symbol="INFY",
            stock_name="Infosys",
            isin="INE009A01021",
            quantity=50,
            market_price=Decimal("1800"),
            market_value=Decimal("90000"),
        ),

        Holding(
            symbol="TCS",
            stock_name="TCS",
            isin="INE467B01029",
            quantity=25,
            market_price=Decimal("4000"),
            market_value=Decimal("100000"),
        ),
    ]

    service = InvestmentDNAService()

    dna = service.build(
        transactions,
        holdings,
    )

    assert dna.total_buy_transactions == 2
    assert dna.total_sell_transactions == 1
    assert dna.companies_invested == 2
    assert dna.current_holdings == 2
    assert dna.most_traded_stock == "INFY"
    assert dna.years_investing > 0