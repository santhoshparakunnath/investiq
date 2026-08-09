from app.validators.icici_tradebook_validator import (
    ICICIDirectTradebookValidator,
)


def test_invalid_quantity():

    row = {
        "Date": "03-Sep-2021",
        "Stock": "INFY",
        "Action": "BUY",
        "Qty": 0,
        "Price": 1500,
        "Exchange": "NSE",
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 1
    assert errors[0].field == "Qty"
    assert errors[0].message == "Quantity must be greater than zero."


def test_invalid_price():

    row = {
        "Date": "03-Sep-2021",
        "Stock": "INFY",
        "Action": "BUY",
        "Qty": 10,
        "Price": 0,
        "Exchange": "NSE",
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 1

    assert errors[0].field == "Price"
    assert errors[0].message == "Price must be greater than zero."

def test_invalid_date():

    row = {
        "Date": "31-Feb-2021",
        "Stock": "INFY",
        "Action": "BUY",
        "Qty": 100,
        "Price": 1500,
        "Exchange": "NSE",
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 1
    assert errors[0].field == "Date"
    assert errors[0].message == "Invalid date."   

def test_missing_required_fields():

    row = {  }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 6

    fields = [error.field for error in errors]

    assert "Date" in fields
    assert "Stock" in fields
    assert "Action" in fields
    assert "Qty" in fields
    assert "Price" in fields
    assert "Exchange" in fields

def test_invalid_action():

    row = {
        "Date": "03-Sep-2021",
        "Stock": "INFY",
        "Action": "test",
        "Qty": 100,
        "Price": 1500,
        "Exchange": "NSE",
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 1

    assert errors[0].field == "Action"
    assert errors[0].message == "Invalid action."      