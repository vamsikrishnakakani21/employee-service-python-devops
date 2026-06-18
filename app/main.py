from fastapi import FastAPI, HTTPException

from app.models import Employee
from app.service import get_all_employees, get_employee, add_employee

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/version")
def version():
    return {"version": "1.0"}


@app.get("/employees")
def employees():
    return get_all_employees()


@app.get("/employees/{emp_id}")
def employee(emp_id: int):
    result = get_employee(emp_id)

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")

    return result


@app.post("/employees")
def create_employee(employee: Employee):
    return add_employee(employee)
