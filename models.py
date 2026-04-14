from sqlalchemy import Column, Integer, String 
from database import Base
class Mink(Base): tablename = "minks"
id = Column(Integer, primary_key=True, index=True) 
female_no = Column(String, index=True) 
year = Column(Integer) 
quality = Column(String) 
last_year_kids = Column(Integer) 
this_year_kids = Column(Integer) 
shed = Column(String) 
colour = Column(String)
