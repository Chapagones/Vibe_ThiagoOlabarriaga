from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from database import engine
#from models import Base

Base = declarative_base()
#Base.metadata.create_all(bind=engine)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))
    salary = Column(DECIMAL(10,2))