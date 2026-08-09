from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """
    Base class for tradebook validators.
    """

    @abstractmethod
    def validate(self, row) -> list[str]:
        """
        Validate a tradebook row.

        Returns:
            List of validation errors.
            Empty list means the row is valid.
        """
        raise NotImplementedError