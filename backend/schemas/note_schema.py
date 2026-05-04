from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    user_id: str
    content: str

class NoteResponse(BaseModel):
    id: int
    user_id: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True