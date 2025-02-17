from datetime import datetime
from pydantic import BaseModel

class LogModel(BaseModel):
    timestamp: datetime
    error_level: str
    error_message: str

    def __str__(self):
        return f"{self.timestamp} [{self.error_level}] {self.error_message}"