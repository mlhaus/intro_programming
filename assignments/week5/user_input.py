"""
This module contains functions for getting user input from the keyboard
"""

from datetime import date, datetime
import math
import ui_helpers

def get_choice(options: list) -> int:
    """
    This function prompts the user for a choice
    Inputs: a list of string options
    Output: The value entered by the user
    """
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    print()
    return get_int("Choice", True, 1, len(options))

def get_float(prompt: str, required = True, min = -math.inf, max = math.inf) -> float:
    """
    This function prompts the user for a decimal (float) number
    Inputs: prompt (required) - a text string asking the user a question,
        min - the lowest accepted value,
        max - the highest accepted value
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    value = 0
    minSet = min != -math.inf
    maxSet = max != math.inf
    while(True):
        print(prompt, end="")
        # ternary operator - one line if-else statement
        print(" (*)" if required else "", end="")
        if (minSet):
            print(f" [min {min}", end="")
        if (maxSet):
            print(f"- max {max}]", end="")
        if (minSet and not maxSet):
            print("]", end="")
        print(": ", end="")
        try:
            value = float(input())
        except ValueError:
            if(not required):
                value = None
                break
            ui_helpers.show_error("Invalid float value")
            continue

        if(value < min):
            ui_helpers.show_error("Value too low")
            continue
        if (value > max):
            ui_helpers.show_error("Value too high")
            continue
        break
    return value

def get_int(prompt: str, required = True, min = -math.inf, max = math.inf) -> int:
    """
    This function prompts the user for a whole (int) number
    Inputs: prompt (required) - a text string asking the user a question,
        min - the lowest accepted value,
        max - the highest accepted value
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    value = 0
    minSet = min != -math.inf
    maxSet = max != math.inf
    while (True):
        print(prompt, end="")
        # ternary operator - one line if-else statement
        print(" (*)" if required else "", end="")
        if (minSet):
            print(f" [min {min}", end="")
        if (maxSet):
            print(f"- max {max}]", end="")
        if (minSet and not maxSet):
            print("]", end="")
        print(": ", end="")
        try:
            value = int(input())
        except ValueError:
            if (not required):
                value = None
                break
            ui_helpers.show_error("Invalid integer value")
            continue

        if (value < min):
            ui_helpers.show_error("Value too low")
            continue
        if (value > max):
            ui_helpers.show_error("Value too high")
            continue
        break
    return value

def get_str(prompt: str, required = True) -> str:
    """
    This function prompts the user for a string
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    value = 0
    while (True):
        print(prompt, end="")
        # ternary operator - one line if-else statement
        print(" (*)" if required else "", end="")
        print(": ", end="")
        value = input().strip()
        if (value == "" and not required):
            value = None
            break
        elif (value == "" and required):
            ui_helpers.show_error("Value is required")
            continue
        break
    return value

# date source https://stackoverflow.com/a/31972447/6629315
def get_date(prompt: str, required = True, min = datetime.min, max = datetime.max) -> datetime:
    """
    This function prompts the user for date
    Inputs: prompt (required) - a text string asking the user a question,
        min - the lowest accepted value,
        max - the highest accepted value
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    value = 0
    minSet = min != datetime.min
    maxSet = max != datetime.max
    while (True):
        print(prompt, end="")
        # ternary operator - one line if-else statement
        print(" (*)" if required else "", end="")
        print(" [YYYY-MM-DD]", end="")
        if (minSet):
            # Source: https://stackoverflow.com/a/2158454/6629315
            print(f" [min {min.strftime('%Y-%m-%d')}", end="")
        if (maxSet):
            print(f", max {max.strftime('%Y-%m-%d')}]", end="")
        if (minSet and not maxSet):
            print("]", end="")
        print(": ", end="")
        try:
            # Source: https://stackoverflow.com/a/5220024/6629315
            value = datetime.strptime(input(),'%Y-%m-%d')
        except ValueError:
            if (not required):
                value = None
                break
            ui_helpers.show_error("Invalid date value")
            continue

        if (value < min):
            ui_helpers.show_error("Value too low")
            continue
        if (value > max):
            ui_helpers.show_error("Value too high")
            continue
        break
    return value

def get_bool(prompt, required = True) -> bool:
    while (True):
        print(prompt + " [Yes or No]", end="")
        # ternary operator - one line if-else statement
        print(" (*)" if required else "", end="")
        print(": ", end="")
        value = input().strip().lower()
        if (value == "" and not required):
            return None
        elif (value == "" and required):
            ui_helpers.show_error("Value is required")
            continue
        elif (value in ["yes","y"]):
            return True
        elif (value in ["no", "n"]):
            return False
        else:
            ui_helpers.show_error("Invalid value")
            continue

if __name__ == "__main__":
    print(get_bool("Do you like pizza?"))
    print(get_bool("Do you like pizza?", False))
    # get_float("Extra withholding", True, 0)
    # get_int("Number of dependents", True, 0, 10)
    # get_date("Birthday")
    # get_date("Birthday", False)
    # get_date("Event date", True, datetime.now())
    # get_date("Birthday", True, datetime(1900, 1, 1))
    # get_date("Birthday", True, datetime(1900, 1, 1), datetime.now())
    # get_str("Name")