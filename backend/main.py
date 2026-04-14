from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

import models, schemas, crud
from database import Base, engine, SessionLocal

# إنشاء الجداول
Base.metadata.create_all(bind=engine)

app = FastAPI()

# =======================
# CORS (مهم للـ JS)
# =======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =======================
# Static Frontend files
# =======================
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# =======================
# ROOT (Frontend page)
# =======================
@app.get("/")
def home():
    return FileResponse("frontend/index.html")


# =======================
# DB Dependency
# =======================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =======================
# CREATE
# =======================
@app.post("/minks")
def add_mink(mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.create_mink(db, mink)


# =======================
# READ ALL
# =======================
@app.get("/minks")
def get_minks(db: Session = Depends(get_db)):
    return crud.get_all(db)


# =======================
# UPDATE
# =======================
@app.put("/minks/{id}")
def edit_mink(id: int, mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.update_mink(db, id, mink)


# =======================
# DELETE
# =======================
@app.delete("/minks/{id}")
def delete_mink(id: int, db: Session = Depends(get_db)):
    crud.delete_mink(db, id)
    return {"status": "deleted"}


# =======================
# SEARCH
# =======================
@app.get("/search")
def search(
    female_no: str = None,
    shed: str = None,
    min_kids: int = None,
    colour: str = None,
    db: Session = Depends(get_db)
):
    return crud.search_minks(db, female_no, shed, min_kids, colour)
