from user_input import get_float, get_int, get_str, get_date
from datetime import datetime
from ui_helpers import show_program_title
import employee_handlers as eh
'''
This is the main module for the Employee demo project
'''

def main():
    """
    Description: Displays a menu in a loop, responding to the user's inputs until the user chooses to quit
    Input: none
    Output: none
    """
    show_program_title("Employee Program")
    choice = get_int("Choice", False, 1, 6)
    eh.add_employee()
    eh.get_employee()
    eh.get_all_employees()
    eh.update_employee()
    eh.delete_employee()
    
    
    
if __name__ == "__main__":
    main()