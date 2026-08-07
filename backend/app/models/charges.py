from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Charges:
    """
    Represents all charges associated with a trade.
    """

    brokerage: Decimal = Decimal("0.00")
    stt: Decimal = Decimal("0.00")
    gst: Decimal = Decimal("0.00")
    stamp_duty: Decimal = Decimal("0.00")
    exchange_charges: Decimal = Decimal("0.00")
    sebi_charges: Decimal = Decimal("0.00")

    @property
    def total(self) -> Decimal:
        return (
            self.brokerage
            + self.stt
            + self.gst
            + self.stamp_duty
            + self.exchange_charges
            + self.sebi_charges
        )