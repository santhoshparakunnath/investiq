from dataclasses import dataclass


@dataclass
class BuyingBehaviorAnalysis:
    """
    Summary of an investor's buying behaviour.
    """

    total_buy_transactions: int
    repeat_purchase_count: int
    averaging_down_count: int
    averaging_up_count: int
    same_price_count: int