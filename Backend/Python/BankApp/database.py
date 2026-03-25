from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:Kolbach14!@localhost:3306/employee_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)