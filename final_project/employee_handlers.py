from final_project.ui_helpers import show_message
from ui_helpers import show_section_title
from user_input import get_str, get_date, get_int, get_bool, get_float
from table import print_table
import copy
'''
This module contains functions related to creating, reading, updating, and deleting employee records
'''

employees = []

def add_employee():
    """
    Handles logic for adding one employee record
    INPUTS: None
    OUTPUT: None
    """
    get_employee_data()
    get_all_employees()

def get_employee_data() -> None:
    """
    Prompt the user for the employee's name (first, last), dob, dependents, extra withholding
    INPUTS: None
    OUTPUT: None
    """
    list = []
    list.append(get_str("First Name"))
    list.append(get_str("Last Name"))
    list.append(get_date("Date of Birth"))
    list.append(get_int("Number of Dependents"))
    list.append(get_float("Extra Withholding?"))
    list.append(get_float("Cost?"))
    list.append(get_int("Expected Attendance?"))
    list.append(get_str("Free?"))
    employees.append(list)
    

def get_all_employees():
    """
    Handles logic for getting all employee records
    INPUTS: None
    OUTPUT: None
    """
    if(len(employees) > 0):
        header = ["First Name", "Last Name", "Date of Birth", "Number Dependents", "Extra Withholding", "Cost", "Attendance", "Free?"]
        # copy_employees = copy.deepcopy(employees)
        # Source: https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column
        copy_employees = sorted(employees,key=lambda x: x[1]) # sort employees last name A-Z, add ", reverse=True" to reverse the order
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