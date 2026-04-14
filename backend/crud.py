from backend.models import Mink
#CREATE
def create_mink(db, data): 
    mink = Mink(**data.dict()) 
    db.add(mink) 
    db.commit() 
    db.refresh(mink) 
    return mink
#READ ALL
def get_all(db): 
    return db.query(Mink).all()
#DELETE
def delete_mink(db, id): 
    m = db.query(Mink).get(id) 
    if m: db.delete(m) 
    db.commit()
#UPDATE
def update_mink(db, id, data): 
    m = db.query(Mink).get(id) 
    if not m: 
        return None 
    for key, value in data.dict().items(): 
        setattr(m, key, value) 
        db.commit() 
        db.refresh(m) 
        return m
#SEARCH + FILTER
from sqlalchemy import and_
def search_minks(db, female_no=None, shed=None, min_kids=None, colour=None):
    query = db.query(Mink)
    if female_no: 
        query = query.filter(Mink.female_no.contains(female_no)) 
    if shed: 
        query = query.filter(Mink.shed == shed) 
    if min_kids: 
        query = query.filter(Mink.this_year_kids >= min_kids) 
    if colour:
        query = query.filter(Mink.colour.contains(colour)) 

    return query.all() 