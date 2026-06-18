from app.data import employees


def get_all_employees():
    return list(employees.values())


def get_employee(emp_id: int):
    return employees.get(emp_id)


def add_employee(employee):
    employees[employee.id] = employee.model_dump()
    return employee
