from dataclasses import dataclass


@dataclass
class SellingBehaviorAnalysis:
    """
    Summary of an investor's selling behaviour.
    """

    total_sell_transactions: int
    profit_taking_count: int
    loss_taking_count: int
    partial_sale_count: int
    complete_exit_count: int