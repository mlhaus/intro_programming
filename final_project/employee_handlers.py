from ui_helpers import show_message
from user_input import get_str, get_date, get_int, get_bool, get_float
from table import print_table
from employee_data import get_data, add_data, get_employee_by_id, update_data, delete_data
from datetime import datetime
'''
This module contains functions related to creating, reading, updating, and deleting employee records
'''

HEADER = ["ID", "First Name", "Last Name", "Date of Birth", "Number Dependents", "Extra Withholding"]

def add_employee():
    """
    Handles logic for adding one employee record
    INPUTS: None
    OUTPUT: None
    """
    employee_list = get_employee_data()
    add_data(employee_list)

def get_employee_data() -> None:
    """
    Prompt the user for the employee's name (first, last), dob, dependents, extra withholding
    INPUTS: None
    OUTPUT: List of data input
    """
    list = []
    list.append(get_int("ID", True, 1))
    list.append(get_str("First Name"))
    list.append(get_str("Last Name"))
    list.append(get_date("Date of Birth", True).strftime('%Y-%m-%d'))
    list.append(get_int("Number of Dependents", True, 0))
    list.append(get_float("Extra Withholding?", True, 0))
    return list
    

def get_all_employees():
    """
    Handles logic for getting all employee records
    INPUTS: None
    OUTPUT: None
    """
    employees = get_data()
    if(len(employees) > 0):
        copy_employees = sorted(employees, key=lambda x: x[2])
        copy_employees.insert(0, HEADER)
        print_table(copy_employees)
    else:
        show_message("There are no employees to show", "alert")


def get_employee():
    """
    Handles logic for getting one employee record
    INPUTS: None
    OUTPUT: None
    """
    emp_id = get_int("Enter the employee ID")
    employees = get_employee_by_id(emp_id)
    if(len(employees) == 0):
        show_message(f"No employees found with id '{emp_id}'", "alert")
    else:
        copy_employees = sorted(employees, key=lambda x: x[2])
        copy_employees.insert(0, HEADER)
        print_table(copy_employees)
        return employees

def update_employee():
    """
    Handles logic for updating one employee record
    INPUTS: None
    OUTPUT: None
    """
    employee_list = get_employee()[0]
    if(len(employee_list) == 0):
        show_message(f"No employees found", "alert")
    else:
        show_message("Press enter to keep the existing value")

        first_name = employee_list[1]
        new_first_name = get_str(f"First name ({first_name})", False)
        if(new_first_name != None and new_first_name != ""):
            employee_list[1] = new_first_name

        last_name = employee_list[2]
        new_last_name = get_str(f"Last name ({last_name})", False)
        if (new_last_name != None and new_last_name != ""):
            employee_list[2] = new_last_name

        date_of_birth = employee_list[3]
        new_date_of_birth = get_date(f"Birthday ({date_of_birth})", False)
        if (new_date_of_birth != None):
            employee_list[3] = new_date_of_birth.strftime('%Y-%m-%d')

        number_dependents = employee_list[4]
        new_number_dependents = get_int(f"Number of Dependents ({number_dependents})", False, 0, 10)
        if (new_number_dependents != None):
            employee_list[4] = new_number_dependents

        extra_withholding = employee_list[5]
        new_extra_withholding = get_float(f"Extra Withholding ({extra_withholding})", False, 0)
        if (new_extra_withholding != None):
            employee_list[5] = new_extra_withholding

        update_data(employee_list)


def delete_employee():
    """
    Handles logic for deleting one employee record
    INPUTS: None
    OUTPUT: None
    """
    employee_list = get_employee()[0]
    if (len(employee_list) == 0):
        show_message(f"No employees found", "alert")
    else:
        resp = get_bool(f"Are you sure you want to delete {employee_list[1]} {employee_list[2]}?")
        if(resp == True):
            delete_data(employee_list)