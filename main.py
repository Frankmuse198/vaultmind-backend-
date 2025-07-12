from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uuid

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

notes_db = {}

@app.get("/")
def read_root():
    return {"VaultMind": "API is live and private"}

@app.post("/note")
def create_note(note: Note):
    note_id = str(uuid.uuid4())
    notes_db[note_id] = note
    return {"note_id": note_id, "message": "Note stored securely"}

@app.get("/note/{note_id}")
def get_note(note_id: str):
    return notes_db.get(note_id, {"error": "Not found"})

@app.post("/summarize")
async def summarize_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "summary": "Summary to be generated here"}
