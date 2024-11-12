from ui_helpers import show_message, press_enter_to_continue, show_menu
from ui_helpers import show_program_title, show_error, show_section_title
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
    menu_options = ["Add an employee", "Get all employees", "Get single employee", "Update employee", "Delete Employee", "Quit"]
    while(not done):
        choice = show_menu("Main Menu", menu_options)
        # Display a section title for all but the last option
        if(choice < len(menu_options)):
            show_section_title(menu_options[choice - 1])
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
            # TODO: prompt the user to confirm that they want to quit
            # If the user chooses no, call a continue statement to restart the loop
            # If the user chooses yes, call the break statement to end the loop
            break
        else:
            show_error("Invalid choice.")
        press_enter_to_continue()
    show_message("Program Complete. Have a great day!")
    
    
if __name__ == "__main__":
    main()