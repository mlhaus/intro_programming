def show_message(message: str, type = "") -> None:
    """
    Displays a message
    INPUTS:
        message, A string with the text to display
        type, A string such as "error", "title", etc.
    OUTPUT: None
    """
    print("\n" + (type.upper() + ":" if(type != "") else "") + message)


def show_error(message: str) -> None:
    """
    Displays an error message and then requests that the user press Enter to continue
    INPUTS: message, A string with the error message
    OUTPUT: None
    """
    show_message(message, "error")
