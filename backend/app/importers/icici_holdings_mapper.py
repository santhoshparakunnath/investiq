from decimal import Decimal

from app.importers.icici_holdings_columns import (
    STOCK_NAME,
    SYMBOL,
    ISIN,
    QUANTITY,
    MARKET_PRICE,
    MARKET_VALUE,
)

from app.models.holding import Holding


class ICICIDirectHoldingsMapper:
    """
    Maps one ICICI Direct Holdings row into a Holding.
    """

    def to_holding(self, row) -> Holding:

        return Holding(
            symbol=str(row[SYMBOL]).strip(),

            stock_name=str(row[STOCK_NAME]).strip(),

            isin=str(row[ISIN]).strip(),

            quantity=int(row[QUANTITY]),

            market_price=Decimal(str(row[MARKET_PRICE])),

            market_value=Decimal(str(row[MARKET_VALUE])),
        )