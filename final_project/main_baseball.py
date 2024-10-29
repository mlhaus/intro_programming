from ui_helpers import show_message, press_enter_to_continue
from user_input import get_choice
from ui_helpers import show_program_title, show_error, show_section_title
import baseball_handlers as bh

'''
This is the main module for the Employee demo project
'''


def main():
    """
    Description: Displays a menu in a loop, responding to the user's inputs until the user chooses to quit
    Input: none
    Output: none
    """
    show_program_title("Baseball Team Program")
    done = False
    menu_options = ["Add a team", "Get all teams", "Get single team", "Update team", "Delete team",
                    "Quit"]
    while (not done):
        choice = get_choice(menu_options)
        show_section_title(menu_options[choice - 1])
        if (choice == 1):
            bh.add_team()
        elif (choice == 2):
            bh.get_all_teams()
        elif (choice == 3):
            bh.get_team()
        elif (choice == 4):
            bh.update_team()
        elif (choice == 5):
            bh.delete_team()
        elif (choice == 6):
            # To do: prompt the user to confirm that they want to quit
            break
        else:
            show_error("Invalid choice.")
        press_enter_to_continue()
    show_message("Program Complete. Have a great day!")


if __name__ == "__main__":
    main()