from ui_helpers import show_message
from user_input import get_str, get_date, get_int, get_bool, get_float
from table import print_table
from employee_data import get_data, add_data
'''
This module contains functions related to creating, reading, updating, and deleting employee records
'''

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
    list.append(get_int("ID"))
    list.append(get_str("First Name"))
    list.append(get_str("Last Name"))
    list.append(get_date("Date of Birth"))
    list.append(get_int("Number of Dependents"))
    list.append(get_float("Extra Withholding?"))
    return list
    

def get_all_employees():
    """
    Handles logic for getting all employee records
    INPUTS: None
    OUTPUT: None
    """
    employees = get_data()
    if(len(employees) > 0):
        header = ["ID","First Name", "Last Name", "Date of Birth", "Number Dependents", "Extra Withholding"]
        copy_employees =  sorted(sorted(employees, key=lambda x: x[2]), key=lambda x: x[1])
        copy_employees.insert(0, header)
        print_table(copy_employees)
    else:
        show_message("There are no employees to show", "alert")


def get_employee():
    """
    Handles logic for getting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def update_employee():
    """
    Handles logic for updating one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def delete_employee():
    """
    Handles logic for deleting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass