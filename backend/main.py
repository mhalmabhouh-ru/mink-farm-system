import os
from pathlib import Path
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from backend import models, schemas, crud
from backend.database import Base, engine, SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/minks")
def add_mink(mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.create_mink(db, mink)


@app.get("/minks")
def get_minks(db: Session = Depends(get_db)):
    return crud.get_all(db)


@app.put("/minks/{id}")
def edit_mink(id: int, mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.update_mink(db, id, mink)


@app.delete("/minks/{id}")
def delete_mink(id: int, db: Session = Depends(get_db)):
    crud.delete_mink(db, id)
    return {"status": "deleted"}
