from pydantic import BaseModel

class FilePayload(BaseModel):
    path: str       # relative to BASE_DIR
    content: str    # file content to write
