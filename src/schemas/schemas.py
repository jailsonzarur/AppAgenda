from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    name: str
    description: str
    date: str
    startTime: str
    endTime: str

    class Config:
        from_attributes = True

