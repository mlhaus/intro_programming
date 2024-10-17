from final_project.ui_helpers import show_message, press_enter_to_continue
from user_input import get_float, get_int, get_str, get_date
from ui_helpers import show_program_title, show_error
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
    done = False
    while(not done):
        choice = get_int("Choice", False, 1, 6)
        if(choice == 1):
            eh.add_employee()
        elif(choice == 2):
            eh.get_all_employees()
        elif(choice == 3):
            eh.get_employee()
        elif(choice == 4):
            eh.update_employee()
        elif(choice == 5):
            eh.delete_employee()
        elif(choice == 6):
            # To do: prompt the user to confirm that they want to quit
            break
        else:
            show_error("Invalid choice.")
        press_enter_to_continue()
    show_message("Program Complete. Have a great day!")
    
    
if __name__ == "__main__":
    main()