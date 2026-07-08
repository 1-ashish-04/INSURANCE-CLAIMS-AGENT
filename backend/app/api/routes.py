import os
import shutil

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException

from app.utils.file_loader import FileLoader

router = APIRouter()


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):

    try:

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = FileLoader.load(file_path)

        return {
            "filename": file.filename,
            "text": extracted_text
        }

    except Exception as e:
        raise HTTPException(
        status_code=400,
        detail=str(e)
    )