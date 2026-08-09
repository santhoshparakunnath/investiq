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

    assert "Quantity must be greater than zero." in errors


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

    assert "Price must be greater than zero." in errors

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

    assert "Invalid date." in errors    

def test_missing_required_fields():

    row = {  }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 6

    assert "Date is required." in errors
    assert "Stock is required." in errors
    assert "Action is required." in errors
    assert "Qty is required." in errors
    assert "Price is required." in errors
    assert "Exchange is required." in errors

def test_invalid_action():

    row = {
        "Date": "31-Feb-2021",
        "Stock": "INFY",
        "Action": "test",
        "Qty": 100,
        "Price": 1500,
        "Exchange": "NSE",
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert "Invalid action." in errors           