from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel

from src.domain import File, FileType
from src.classifiers.file_classifier import FileClassifier


app = FastAPI()

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


class ClassifiedFile(BaseModel):
    file_type: FileType


@app.post("/classify_file")
async def classify_file(file: UploadFile) -> ClassifiedFile:
    if file.filename == "" or file.filename is None:
        raise HTTPException(400, "No filename on file")

    f = File(name=file.filename, content=file.file)
    if f.extension() not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"Filetype not allowed: {f.extension()}")

    file_type = FileClassifier().classify_file(f)

    return ClassifiedFile(file_type=file_type)
