from data_helpers import process_file, write_file
from ui_helpers import show_message

FILE_NAME = "employees.csv"
NEEDED_FIELDS = ["ID","First Name","Last Name","Date of Birth","Number of Dependents","Extra Withholding"]

def get_data():
    """
    Get existing data from a text file
    Inputs: None
    Outputs: A list of employees
    """
    employees = process_file(FILE_NAME, NEEDED_FIELDS)
    return employees

def get_employee_list():
    """
    Inputs: None
    Outputs: The formatted list of employees
    """
    employees = get_data()
    formatted_employees = []
    for employee in employees:
        record = []
        record.append(int(employee[0])) # Format the string id to int
        record.append(employee[1]) # First name
        record.append(employee[2]) # Last name
        record.append(employee[3]) # Date of birth
        record.append(int(employee[4])) # Number of Dependents
        record.append(float(employee[5])) # Extra Withholding
        formatted_employees.append(record)
    return formatted_employees

def add_data(employee: list):
    """
    Input: A single employee
    Output: A list containing all of the employees
    """
    employee_list = get_employee_list()
    employee_list.append(employee)
    write_file(FILE_NAME, NEEDED_FIELDS, employee_list)
    show_message("Employee added", "success")


if __name__ == "__main__":
    print(get_data())