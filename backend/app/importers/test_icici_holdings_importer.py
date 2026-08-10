from decimal import Decimal

from app.importers.icici_holdings_importer import (
    ICICIDirectHoldingsImporter,
)


def test_import_holdings():

    importer = ICICIDirectHoldingsImporter()

    holdings = importer.import_holdings(
        "sample_data/8501105311_Demat.csv"
    )

    assert len(holdings) > 0

    first = holdings[0]

    assert first.symbol is not None
    assert first.stock_name is not None
    assert first.isin is not None

    assert first.quantity > 0

    assert first.market_price > Decimal("0")

    assert first.market_value > Decimal("0")