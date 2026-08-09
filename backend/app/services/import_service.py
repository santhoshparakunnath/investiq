from fastapi import UploadFile

from app.importers.icici_direct_importer import ICICIDirectImporter
from app.importers.icici_direct_mapper import ICICIDirectMapper


class ImportService:

    async def import_file(self, file: UploadFile):

        importer = ICICIDirectImporter()
        mapper = ICICIDirectMapper()

        df = importer.load(file.file)

        transaction = mapper.to_transaction(df.iloc[0])

        return {
            "filename": file.filename,
            "transaction": transaction
        }