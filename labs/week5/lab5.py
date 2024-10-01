'''
FILE:	lab_05.py
DATE:	2024-09-26
AUTHOR: Marc Hauschildt
DESCRIPTION:
	This is the start of a menu-driven program that allows a Human Resources (HR)
        clerk to manage employee data records.
'''
# Define all the hard-coded strings.
program_title = "*** Employee Program ***"
main_menu_title = "-- Main Menu --"
add_employee = "Add an Employee"
show_all_employees = "Show All Employees"
view_employee = "View an Employee"
update_employee = "Update an Employee"
delete_employee = "Delete an Employee"
quit = "Quit"
menu_prompt = "Your choice: "
choice_response = "You chose to"
error_response = "Your choice was not recognized.  Please try again."
press_enter = "Press the Enter key to continue..."
program_complete = "Program complete."
CONSOLE_WIDTH = 80

done = False
while(not done):
    print(f"{program_title:^{CONSOLE_WIDTH}}\n")
    print(f"{main_menu_title:^{CONSOLE_WIDTH}}\n")
    print(f"1.\t\t{add_employee}")
    print(f"2.\t\t{show_all_employees}")
    print(f"3.\t\t{view_employee}")
    print(f"4.\t\t{update_employee}")
    print(f"5.\t\t{delete_employee}")
    print(f"6.\t\t{quit}")

    # Prompt the user for input
    choice = int(input(menu_prompt))
    # Display output
    if(choice == 1):
        print(f"{choice_response} {add_employee.lower()}")
    elif(choice == 2):
        print(f"{choice_response} {show_all_employees.lower()}")
    elif(choice == 3):
        print(f"{choice_response} {view_employee.lower()}")
    elif(choice == 4):
        print(f"{choice_response} {update_employee.lower()}")
    elif(choice == 5):
        print(f"{choice_response} {delete_employee.lower()}")
    elif(choice == 6):
        done = True
        continue
    else:
        print(error_response)

    input(f"\n{press_enter}\n")

print(program_complete)
