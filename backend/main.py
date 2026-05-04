from fastapi import FastAPI
from backend.routers import note_router

app = FastAPI(title="Notes App API")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Kết nối router vào app chính
app.include_router(note_router.router)