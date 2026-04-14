from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models, schemas, crud

app = FastAPI()

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE TABLES (OK هنا لكن الأفضل لاحقًا ننقله)
Base.metadata.create_all(bind=engine)

# CREATE
@app.post("/minks")
def add_mink(mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.create_mink(db, mink)

# READ
@app.get("/minks")
def get_minks(db: Session = Depends(get_db)):
    return crud.get_all(db)

# UPDATE
@app.put("/minks/{id}")
def edit_mink(id: int, mink: schemas.MinkCreate, db: Session = Depends(get_db)):
    return crud.update_mink(db, id, mink)

# DELETE
@app.delete("/minks/{id}")
def remove(id: int, db: Session = Depends(get_db)):
    crud.delete_mink(db, id)
    return {"status": "deleted"}

# SEARCH
@app.get("/search")
def search(
    female_no: str = None,
    shed: str = None,
    min_kids: int = None,
    colour: str = None,
    db: Session = Depends(get_db)
):
    return crud.search_minks(db, female_no, shed, min_kids, colour)
