from pydantic import BaseModel

class TerminalPayload(BaseModel):
    command: str    # shell command to execute
