from datetime import datetime

from app.models.validation_error import ValidationError
from app.validators.base_validator import BaseValidator


class ICICIDirectTradebookValidator(BaseValidator):

    REQUIRED_FIELDS = [
        "Date",
        "Stock",
        "Action",
        "Qty",
        "Price",
        "Exchange",
    ]

    def validate(self, row) -> list[ValidationError]:

        validation_errors = []

        # Validate required fields
        for field in self.REQUIRED_FIELDS:

            value = row.get(field)

            if value is None or str(value).strip() == "":
                validation_errors.append(
                    ValidationError(
                        field=field,
                        message=f"{field} is required."
                    )
                )

        # Validate Action
        action = str(row.get("Action", "")).strip().upper()

        if action and action not in ["BUY", "SELL"]:
            validation_errors.append(
                ValidationError(
                    field="Action",
                    message="Invalid action."
                )
            )

        # Validate Quantity
        quantity = row.get("Qty")

        if quantity is not None and quantity <= 0:
            validation_errors.append(
                ValidationError(
                    field="Qty",
                    message="Quantity must be greater than zero."
                )
            )

        # Validate Price
        price = row.get("Price")

        if price is not None and price <= 0:
            validation_errors.append(
                ValidationError(
                    field="Price",
                    message="Price must be greater than zero."
                )
            )

        # Validate Date
        date_value = str(row.get("Date", "")).strip()

        if date_value:
            valid_date = False

            for date_format in (
                "%d-%b-%Y",
                "%d-%m-%Y",
                "%d-%b-%y",
            ):
                try:
                    datetime.strptime(date_value, date_format)
                    valid_date = True
                    break
                except ValueError:
                    continue

            if not valid_date:
                validation_errors.append(
                    ValidationError(
                        field="Date",
                        message="Invalid date."
                    )
                )

        return validation_errors