from abc import ABC, abstractmethod

from app.models.import_result import ImportResult


class BaseImporter(ABC):
    """
    Base class for all broker importers.
    """

    @abstractmethod
    def can_import(self, file) -> bool:
        """
        Returns True if this importer can process the uploaded file.
        """
        pass

    @abstractmethod
    def import_data(self, file) -> list:
        """
        Imports data from the broker.
        """
        pass