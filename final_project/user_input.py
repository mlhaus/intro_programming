"""
This module contains functions for getting user input from the keyboard
"""

from datetime import date, datetime
import math
from ui_helpers import show_error

def get_choice():
    pass

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
        try:
            print(prompt, end="")
            # ternary operator - one line if-else statement
            print(" (*)" if required else "", end="")
            if(minSet):
                print(f" [min {min}", end="")
            if(maxSet):
                print(f"- max {max}]", end="")
            if(minSet and not maxSet):
                print("]", end="")
            print(": ", end="")
            value = float(input())
        except ValueError:
            if(not required):
                value = None
                break
            show_error("Invalid float value")
            continue

        if(value < min):
            show_error("Value too low")
            continue
        if (value > max):
            show_error("Value too high")
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
        try:
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
            value = int(input())
        except ValueError:
            if (not required):
                value = None
                break
            show_error("Invalid integer value")
            continue

        if (value < min):
            show_error("Value too low")
            continue
        if (value > max):
            show_error("Value too high")
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
        value = input()
        if (value == "" and not required):
            value = None
            break
        elif (value == "" and required):
            show_error("Value is required")
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
    minSet = min != date.min
    maxSet = max != date.max
    while (True):
        try:
            print(prompt, end="")
            # ternary operator - one line if-else statement
            print(" (*)" if required else "", end="")
            print(" [YYYY-MM-DD]", end="")
            # if (minSet):
            #     print(f" [min {min}", end="")
            # if (maxSet):
            #     print(f"- max {max}]", end="")
            # if (minSet and not maxSet):
            #     print("]", end="")
            print(": ", end="")
            # Source: https://stackoverflow.com/a/5220024/6629315
            value = datetime.strptime(input(),'%Y-%m-%d')
        except ValueError:
            if (not required):
                value = None
                break
            show_error("Invalid date value")
            continue

        if (value < min):
            show_error("Value too low")
            continue
        if (value > max):
            show_error("Value too high")
            continue
        break
    return value

def get_bool(prompt) -> bool:
    pass
