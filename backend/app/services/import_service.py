from fastapi import UploadFile


class ImportService:

    async def import_file(self, file: UploadFile):

        content = await file.read()

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(content)
        }