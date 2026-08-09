from app.validators.base_validator import BaseValidator
from datetime import datetime


class ICICIDirectTradebookValidator(BaseValidator):

    REQUIRED_FIELDS = [
        "Date",
        "Stock",
        "Action",
        "Qty",
        "Price",
        "Exchange",
    ]

    def validate(self, row) -> list[str]:

        errors = []

        # Validate required fields
        for field in self.REQUIRED_FIELDS:
            value = row.get(field)

            if value is None or str(value).strip() == "":
                errors.append(f"{field} is required.")

        # Validate Action
        action = str(row.get("Action", "")).strip().upper()

        if action and action not in ["BUY", "SELL"]:
            errors.append("Invalid action.")

        # Validate Quantity
        quantity = row.get("Qty")

        if quantity is not None and quantity <= 0:
            errors.append("Quantity must be greater than zero.")

        # Validate Price
        price = row.get("Price")

        if price is not None and price<= 0:
            errors.append("Price must be greater than zero.")

        # Validate Date
        date_value = str(row.get("Date", "")).strip()

        if date_value:
            try:
                datetime.strptime(date_value, "%d-%b-%Y")
            except ValueError:
                errors.append("Invalid date.")

        action = str(row.get("Action", "")).strip().upper()

        if action and action not in ["BUY", "SELL"]:
            errors.append("Invalid action.")                

        return errors