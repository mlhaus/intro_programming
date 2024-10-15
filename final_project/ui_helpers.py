'''
The functions in this module will help us define User Interface appearance
'''

CONSOLE_WIDTH = 100

def show_program_title(title: str) -> None:
    """
    Displays the formatted program title
    INPUTS: title, A string containing the title of the program
    OUTPUT: None
    """
    show_message(f'\n{"** " + title + " **":^{CONSOLE_WIDTH}}')

def show_section_title(title: str) -> None:
    """
    Displays a section title
    INPUT: title, A string with title of the section
    OUTPUT: None
    """
    show_message(f'{"-- " + title + " --":^{CONSOLE_WIDTH}}')

def show_message(message: str, type = "") -> None:
    """
    Displays a message
    INPUTS:
        message, A string with the text to display
        type, A string such as "error", "title", etc.
    OUTPUT: None
    """
    print("\n" + (type.upper() + ":" if(type != "") else "") + message)

def press_enter_to_continue() -> None:
    """
    Displays a message instructing the user to press  the Enter key and then waits until they do
    INPUT: None
    OUTPUT: None
    """
    input("Press enter to continue...")

def show_error(message: str) -> None:
    """
    Displays an error message and then requests that the user press Enter to continue
    INPUTS: message, A string with the error message
    OUTPUT: None
    """
    show_message(message, "error")
    press_enter_to_continue()

def show_menu(menu_title: str, options: list) -> None:
    """
    Displays the menu title and then displays the menu options, one per line
    INPUTS:
        menu_title, A string with the name of the menu
        options, A list of strings with the options for the menu
    OUTPUT: None
    """
    pass

def confirm_quit() -> bool:
    """ 
    Displays a message stating that the user has chosen to quit. Then asks the user to confirm the desire 
    to quit by entering Y
    INPUT: None
    RETURNS: boolean True if the user confirms the quit, and False otherwise
    """
    pass