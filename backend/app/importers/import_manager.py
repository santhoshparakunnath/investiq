from app.importers.base_importer import BaseImporter
from app.importers.icici_direct_importer import ICICIDirectImporter


class ImportManager:
    """
    Selects the correct importer for an uploaded file.
    """

    def __init__(self):
        self.importers: list[BaseImporter] = [
            ICICIDirectImporter(),
        ]

    def get_importer(self, file) -> BaseImporter:
        for importer in self.importers:
            if importer.can_import(file):
                return importer

        raise ValueError("No suitable importer found.")