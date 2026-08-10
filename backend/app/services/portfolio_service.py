from app.models.transaction import Transaction
from app.models.holding import Holding


class PortfolioService:
    """
    Builds holdings from imported transactions.
    """

    def build_holdings(
        self,
        transactions: list[Transaction]
    ) -> list[Holding]:

        pass