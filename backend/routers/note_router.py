from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies.db import get_db
from backend.schemas.note_schema import NoteCreate, NoteResponse
from backend.services import note_service
from typing import List

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return note_service.create_user_note(db, note)

@router.get("/{user_id}", response_model=List[NoteResponse])
def read_notes(user_id: str, db: Session = Depends(get_db)):
    return note_service.get_user_notes(db, user_id)