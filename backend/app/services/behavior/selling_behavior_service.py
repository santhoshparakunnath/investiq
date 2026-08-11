from app.models.enums import TransactionType
from app.models.selling_behavior_analysis import SellingBehaviorAnalysis
from app.models.transaction import Transaction


class SellingBehaviorService:
    """
    Analyzes an investor's selling behaviour.

    Uses FIFO (First In, First Out) to match sell transactions
    against earlier buy transactions.
    """

    def analyze(
        self,
        transactions: list[Transaction],
    ) -> SellingBehaviorAnalysis:

        total_sell_transactions = 0
        profit_taking_count = 0
        loss_taking_count = 0
        partial_sale_count = 0
        complete_exit_count = 0

        # Store open buy lots by symbol.
        buy_lots = {}

        # Process transactions chronologically.
        sorted_transactions = sorted(
            transactions,
            key=lambda transaction: transaction.trade_date,
        )

        for transaction in sorted_transactions:

            symbol = transaction.symbol

            if symbol not in buy_lots:
                buy_lots[symbol] = []

            # -------------------------
            # BUY
            # -------------------------

            if transaction.action == TransactionType.BUY:

                buy_lots[symbol].append(
                    {
                        "quantity": transaction.quantity,
                        "price": transaction.price,
                    }
                )

            # -------------------------
            # SELL
            # -------------------------

            elif transaction.action == TransactionType.SELL:

                total_sell_transactions += 1

                remaining_quantity = transaction.quantity
                sale_was_partial = False
                sale_was_complete = True

                while (
                    remaining_quantity > 0
                    and buy_lots[symbol]
                ):

                    buy_lot = buy_lots[symbol][0]

                    matched_quantity = min(
                        remaining_quantity,
                        buy_lot["quantity"],
                    )

                    buy_price = buy_lot["price"]
                    sell_price = transaction.price

                    if sell_price > buy_price:
                        profit_taking_count += 1

                    elif sell_price < buy_price:
                        loss_taking_count += 1

                    remaining_quantity -= matched_quantity
                    buy_lot["quantity"] -= matched_quantity

                    if remaining_quantity > 0:
                        sale_was_partial = True

                    if buy_lot["quantity"] == 0:
                        buy_lots[symbol].pop(0)

                    else:
                        sale_was_partial = True

                    if remaining_quantity == 0:
                        break

                # A sale of less than the available position
                # is considered a partial sale.
                if sale_was_partial:
                    partial_sale_count += 1
                else:
                    complete_exit_count += 1

        return SellingBehaviorAnalysis(
            total_sell_transactions=total_sell_transactions,
            profit_taking_count=profit_taking_count,
            loss_taking_count=loss_taking_count,
            partial_sale_count=partial_sale_count,
            complete_exit_count=complete_exit_count,
        )