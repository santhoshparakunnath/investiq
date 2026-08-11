from app.models.enums import TransactionType
from app.models.holding_period_analysis import HoldingPeriodAnalysis
from app.models.transaction import Transaction


class HoldingPeriodService:
    """
    Analyzes how long an investor holds investments.

    Uses FIFO (First In, First Out) to match sell transactions
    against earlier buy transactions.
    """

    def analyze(
        self,
        transactions: list[Transaction],
    ) -> HoldingPeriodAnalysis:

        # Store open buy lots by symbol.
        buy_lots = {}

        # Completed holding periods.
        holding_periods = []

        # Process transactions in chronological order.
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
                        "date": transaction.trade_date,
                        "quantity": transaction.quantity,
                    }
                )

            # -------------------------
            # SELL
            # -------------------------

            elif transaction.action == TransactionType.SELL:

                remaining_quantity = transaction.quantity

                while (
                    remaining_quantity > 0
                    and buy_lots[symbol]
                ):

                    buy_lot = buy_lots[symbol][0]

                    matched_quantity = min(
                        remaining_quantity,
                        buy_lot["quantity"],
                    )

                    holding_days = (
                        transaction.trade_date
                        - buy_lot["date"]
                    ).days

                    holding_periods.append(
                        {
                            "days": holding_days,
                            "quantity": matched_quantity,
                        }
                    )

                    remaining_quantity -= matched_quantity
                    buy_lot["quantity"] -= matched_quantity

                    # Remove the buy lot when completely consumed.
                    if buy_lot["quantity"] == 0:
                        buy_lots[symbol].pop(0)

        # No completed investments.
        if not holding_periods:
            return HoldingPeriodAnalysis(
                average_days=0,
                longest_days=0,
                shortest_days=0,
                completed_positions=0,
            )

        # Calculate quantity-weighted average holding period.
        total_quantity = sum(
            period["quantity"]
            for period in holding_periods
        )

        weighted_days = sum(
            period["days"] * period["quantity"]
            for period in holding_periods
        )

        average_days = weighted_days / total_quantity

        longest_days = max(
            period["days"]
            for period in holding_periods
        )

        shortest_days = min(
            period["days"]
            for period in holding_periods
        )

        return HoldingPeriodAnalysis(
            average_days=average_days,
            longest_days=longest_days,
            shortest_days=shortest_days,
            completed_positions=len(holding_periods),
        )