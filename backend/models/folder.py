from pydantic import BaseModel

class FolderPayload(BaseModel):
    path: str       # relative folder path
