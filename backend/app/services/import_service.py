from fastapi import UploadFile


class ImportService:
    """
    Coordinates the import of broker tradebooks.
    """

    async def import_files(self, files: list[UploadFile]) -> dict:

        return {
            "files_received": len(files)
        }