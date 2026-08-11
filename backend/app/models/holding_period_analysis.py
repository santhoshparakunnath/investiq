from dataclasses import dataclass


@dataclass
class HoldingPeriodAnalysis:
    """
    Summary of an investor's holding period behaviour.
    """

    average_days: float
    longest_days: int
    shortest_days: int
    completed_positions: int