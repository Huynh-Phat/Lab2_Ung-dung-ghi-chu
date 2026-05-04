from sqlalchemy.orm import Session
from backend.core.database import NoteModel
from backend.schemas.note_schema import NoteCreate

def create_user_note(db: Session, note: NoteCreate):
    db_note = NoteModel(user_id=note.user_id, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_user_notes(db: Session, user_id: str):
    return db.query(NoteModel).filter(NoteModel.user_id == user_id).order_by(NoteModel.created_at.desc()).all()