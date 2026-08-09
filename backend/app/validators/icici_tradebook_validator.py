from app.validators.base_validator import BaseValidator


class ICICIDirectTradebookValidator(BaseValidator):

    def validate(self, row) -> list[str]:

        errors = []

        if not str(row["Date"]).strip():
            errors.append("Date is required.")

        return errors