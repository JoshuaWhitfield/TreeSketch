from fastapi import APIRouter, HTTPException
from models.folder import FolderPayload
import os

router = APIRouter()
BASE_DIR = r"D:\Development\PY\CLI\treesketch\core\output"

@router.post("/")
def create_folder(payload: FolderPayload):
    folder_path = os.path.join(BASE_DIR, payload.path)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return {"message": "Folder created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/")
def delete_folder(path: str):
    folder_path = os.path.join(BASE_DIR, path)
    if not os.path.isdir(folder_path):
        raise HTTPException(status_code=404, detail="Folder not found")
    try:
        os.rmdir(folder_path)
        return {"message": "Folder deleted"}
    except OSError:
        raise HTTPException(status_code=400, detail="Folder not empty or cannot be deleted")
