from app.importers.icici_direct_mapper import ICICIDirectMapper
from app.models.enums import TransactionType


def test_map_sell_transaction():

    row = {
        "Date": "03-Sep-2021",
        "Stock": "JSWSTE",
        "Action": "Sell",
        "Qty": 100,
        "Price": 688.52,
        "Trade Value": 68852.3,
        "Order Ref.": "20210903N900062647",
        "Exchange": "NSE",
        "STT": 69,
        "Transaction and SEBI Turnover charges": 1.24,
        "Stamp Duty": 0,
        "Brokerage incl. taxes": 273.5792,
    }

    mapper = ICICIDirectMapper()

    transaction = mapper.to_transaction(row)

    assert transaction.symbol == "JSWSTE"
    assert transaction.quantity == 100
    assert transaction.action == TransactionType.SELL
    assert str(transaction.price) == "688.52"
    assert str(transaction.trade_value) == "68852.3"
    assert transaction.exchange == "NSE"