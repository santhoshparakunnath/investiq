from dataclasses import dataclass


@dataclass
class InvestmentDNA:
    """
    High-level summary of an investor's history and behaviour.
    """

    years_investing: float

    total_buy_transactions: int

    total_sell_transactions: int

    companies_invested: int

    current_holdings: int

    most_traded_stock: str | None = None