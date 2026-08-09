from dataclasses import dataclass


@dataclass
class ValidationError:
    """
    Represents a validation error for a single field.
    """

    field: str
    message: str