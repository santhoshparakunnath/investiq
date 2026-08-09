from abc import ABC, abstractmethod


class BaseValidator(ABC):

    @abstractmethod
    def validate(self, row) -> list[str]:
        """
        Validates a tradebook row.

        Returns:
            A list of validation errors.
            Empty list means the row is valid.
        """
        pass