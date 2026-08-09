from app.validators.icici_tradebook_validator import (
    ICICIDirectTradebookValidator,
)


def test_missing_date():

    row = {
        "Date": ""
    }

    validator = ICICIDirectTradebookValidator()

    errors = validator.validate(row)

    assert len(errors) == 1
    assert errors[0] == "Date is required."