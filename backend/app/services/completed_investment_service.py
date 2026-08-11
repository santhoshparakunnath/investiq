from app.models.completed_investment import CompletedInvestment
from app.models.enums import TransactionType
from app.models.trade_lot import TradeLot
from app.models.transaction import Transaction


class CompletedInvestmentService:
    """
    Builds completed investment lifecycles from transactions.

    Uses FIFO (First In, First Out) to match sell transactions
    against earlier buy lots.
    """

    def build_completed_investments(
        self,
        transactions: list[Transaction],
    ) -> list[CompletedInvestment]:

        buy_lots: dict[str, list[TradeLot]] = {}

        active_investments = {}

        completed_investments = []

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
                    TradeLot(
                        trade_date=transaction.trade_date,
                        quantity=transaction.quantity,
                        price=transaction.price,
                    )
                )

                # Start a new investment lifecycle if necessary.
                if symbol not in active_investments:

                    active_investments[symbol] = {
                        "first_buy_date": transaction.trade_date,
                        "total_quantity": 0,
                        "total_cost": 0,
                        "total_sale_value": 0,
                    }

                active_investments[symbol]["total_quantity"] += (
                    transaction.quantity
                )

                active_investments[symbol]["total_cost"] += (
                    transaction.price * transaction.quantity
                )

            # -------------------------
            # SELL
            # -------------------------

            elif transaction.action == TransactionType.SELL:

                if symbol not in active_investments:
                    continue

                remaining_quantity = transaction.quantity

                while (
                    remaining_quantity > 0
                    and buy_lots[symbol]
                ):

                    buy_lot = buy_lots[symbol][0]

                    matched_quantity = min(
                        remaining_quantity,
                        buy_lot.quantity,
                    )

                    active_investments[symbol]["total_sale_value"] += (
                        transaction.price * matched_quantity
                    )

                    remaining_quantity -= matched_quantity
                    buy_lot.quantity -= matched_quantity

                    if buy_lot.quantity == 0:
                        buy_lots[symbol].pop(0)

                # The investment is complete when no shares remain.
                if not buy_lots[symbol]:

                    investment = active_investments[symbol]

                    first_buy_date = investment["first_buy_date"]
                    final_sell_date = transaction.trade_date

                    holding_days = (
                        final_sell_date - first_buy_date
                    ).days

                    realized_profit = (
                        investment["total_sale_value"]
                        - investment["total_cost"]
                    )

                    completed_investments.append(
                        CompletedInvestment(
                            symbol=symbol,
                            first_buy_date=first_buy_date,
                            final_sell_date=final_sell_date,
                            holding_days=holding_days,
                            total_quantity=investment["total_quantity"],
                            total_cost=investment["total_cost"],
                            total_sale_value=investment["total_sale_value"],
                            realized_profit=realized_profit,
                        )
                    )

                    del active_investments[symbol]

        return completed_investments