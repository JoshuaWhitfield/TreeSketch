from fastapi import APIRouter, HTTPException
from models.file import FilePayload
import os

router = APIRouter()
BASE_DIR = r"D:\Development\PY\CLI\treesketch\core\output"

@router.post("/")
def save_file(payload: FilePayload):
    file_path = os.path.join(BASE_DIR, payload.path)
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(payload.content)
        return {"message": "File saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def read_file(path: str):
    file_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

@router.delete("/")
def delete_file(path: str):
    file_path = os.path.join(BASE_DIR, path)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(file_path)
    return {"message": "File deleted"}
