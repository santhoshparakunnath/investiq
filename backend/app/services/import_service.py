from fastapi import UploadFile

from app.importers.icici_direct_importer import ICICIDirectImporter
from app.importers.icici_direct_mapper import ICICIDirectMapper


class ImportService:

    def import_file(self, file: UploadFile):

        importer = ICICIDirectImporter()

        transactions = importer.import_transactions(file.file)

        return {
            "filename": file.filename,
            "transactions": transactions
        }