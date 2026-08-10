from datetime import date

from app.models.enums import TransactionType
from app.models.holding import Holding
from app.models.investment_dna import InvestmentDNA
from app.models.transaction import Transaction


class InvestmentDNAService:
    """
    Builds an investor's Investment DNA from historical transactions
    and current holdings.
    """

    def build(
        self,
        transactions: list[Transaction],
        holdings: list[Holding],
    ) -> InvestmentDNA:

        if transactions:
            first_trade_date = min(
                transaction.trade_date
                for transaction in transactions
            )

            years_investing = round(
                (date.today() - first_trade_date).days / 365.25,
                1,
            )
        else:
            years_investing = 0

        total_buy_transactions = sum(
            1
            for transaction in transactions
            if transaction.action == TransactionType.BUY
        )

        total_sell_transactions = sum(
            1
            for transaction in transactions
            if transaction.action == TransactionType.SELL
        )

        companies_invested = len(
            {
                transaction.symbol
                for transaction in transactions
            }
        )

        current_holdings = len(holdings)

        if transactions:
            trade_counts = {}

            for transaction in transactions:

                symbol = transaction.symbol

                trade_counts[symbol] = (
                    trade_counts.get(symbol, 0) + 1
                )

            most_traded_stock = max(
                trade_counts,
                key=trade_counts.get,
            )
        else:
            most_traded_stock = None

        return InvestmentDNA(
            years_investing=years_investing,
            total_buy_transactions=total_buy_transactions,
            total_sell_transactions=total_sell_transactions,
            companies_invested=companies_invested,
            current_holdings=current_holdings,
            most_traded_stock=most_traded_stock,
        )