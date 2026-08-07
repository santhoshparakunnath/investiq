from fastapi import APIRouter, UploadFile, File

from app.services.import_service import ImportService

router = APIRouter(prefix="/api/import", tags=["Import"])

service = ImportService()


@router.post("/")
async def import_tradebooks(
    files: list[UploadFile] = File(...)
):
    return await service.import_files(files)