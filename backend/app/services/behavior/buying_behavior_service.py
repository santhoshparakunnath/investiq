from app.models.buying_behavior_analysis import BuyingBehaviorAnalysis
from app.models.enums import TransactionType
from app.models.transaction import Transaction


class BuyingBehaviorService:
    """
    Analyzes an investor's buying behaviour.

    V1 identifies repeat purchases and whether each
    subsequent purchase was made at a lower, higher,
    or equal price than the previous purchase.
    """

    def analyze(
        self,
        transactions: list[Transaction],
    ) -> BuyingBehaviorAnalysis:

        total_buy_transactions = 0
        repeat_purchase_count = 0
        averaging_down_count = 0
        averaging_up_count = 0
        same_price_count = 0

        # Store the most recent buy price for each symbol.
        last_buy_price = {}

        # Process transactions chronologically.
        sorted_transactions = sorted(
            transactions,
            key=lambda transaction: transaction.trade_date,
        )

        for transaction in sorted_transactions:

            if transaction.action != TransactionType.BUY:
                continue

            total_buy_transactions += 1

            symbol = transaction.symbol

            # First purchase of this stock.
            if symbol not in last_buy_price:

                last_buy_price[symbol] = transaction.price

                continue

            # This is a repeat purchase.
            repeat_purchase_count += 1

            previous_price = last_buy_price[symbol]
            current_price = transaction.price

            if current_price < previous_price:
                averaging_down_count += 1

            elif current_price > previous_price:
                averaging_up_count += 1

            else:
                same_price_count += 1

            # Update the previous purchase price.
            last_buy_price[symbol] = current_price

        return BuyingBehaviorAnalysis(
            total_buy_transactions=total_buy_transactions,
            repeat_purchase_count=repeat_purchase_count,
            averaging_down_count=averaging_down_count,
            averaging_up_count=averaging_up_count,
            same_price_count=same_price_count,
        )