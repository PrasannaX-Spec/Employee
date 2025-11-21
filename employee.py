def get_employee_info(
    name, emp_id,department,salary):
        return f"Employee Name: {name},\n ID: {emp_id},\n Department: {department},\n Salary: {salary}"

print(get_employee_info("Prasanna", "EMP001", "IT", 60000))
