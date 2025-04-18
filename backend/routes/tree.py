from fastapi import APIRouter, HTTPException
import os

router = APIRouter()

BASE_DIR = r"D:\Development\PY\CLI\treesketch\core\output"

def walk(dir_path):
    result = {}
    try:
        for entry in os.listdir(dir_path):
            full_path = os.path.join(dir_path, entry)
            if os.path.isdir(full_path):
                result[entry] = walk(full_path)
            else:
                result[entry] = "file"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return result

@router.get("")
@router.get("/")
def get_tree():
    if not os.path.exists(BASE_DIR):
        raise HTTPException(status_code=404, detail="Output directory not found")
    return walk(BASE_DIR)
