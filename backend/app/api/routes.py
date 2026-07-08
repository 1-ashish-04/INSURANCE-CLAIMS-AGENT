import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_loader import FileLoader
from app.services.claim_processor import ClaimProcessor
import uuid

router = APIRouter()

processor = ClaimProcessor()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):

    try:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            filename = f"{uuid.uuid4()}_{file.filename}"
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Read the uploaded file
        document_text = FileLoader.load(file_path)
        os.remove(file_path)

        # Process the claim
        result = processor.process(document_text)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )