from fastapi import APIRouter, HTTPException
from models.terminal import TerminalPayload
import subprocess
import os

router = APIRouter()
BASE_DIR = r"D:\Development\PY\CLI\treesketch\core\output"

@router.post("/")
def run_command(payload: TerminalPayload):
    try:
        result = subprocess.run(
            payload.command,
            cwd=BASE_DIR,
            shell=True,
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
