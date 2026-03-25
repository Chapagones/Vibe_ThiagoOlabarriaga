from models import Employee
from database import SessionLocal


def get_all_employees():
    db = SessionLocal()
    return db.query(Employee).all()

def create_employee(name, department, salary):
    db = SessionLocal()
    emp = Employee(name=name, department=department, salary=salary)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp