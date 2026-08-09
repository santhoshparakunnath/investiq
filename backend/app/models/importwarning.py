from dataclasses import dataclass


@dataclass
class ImportWarning:
    """
    Represents a warning generated while importing a tradebook.
    """

    row_number: int
    field: str
    message: str