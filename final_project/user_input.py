"""
This module contains functions for getting user input from the keyboard
"""

import datetime
import math

def get_float(prompt: str, min = -math.inf, max = math.inf) -> float:
    """
    This function prompts the user for a decimal (float) number
    Inputs: prompt (required) - a text string asking the user a question,
        min - the lowest accepted value,
        max - the highest accepted value
    Output: The value entered by the user
    """
    value = 0
    minSet = min != -math.inf
    maxSet = max != math.inf
    while(True):
        try:
            print(prompt, end="")
            if(minSet):
                print(f" [min {min}", end="")
            if(maxSet):
                print(f"- max {max}]", end="")
            if(minSet and not maxSet):
                print("]", end="")
            print(": ", end="")
            value = float(input())
        except ValueError:
            print("Invalid float value")

        if(value < min):
            print(f"Value too low")
            continue
        if (value > max):
            print(f"Value too high")
            continue
        break
    return value

def get_int(prompt) -> int:
    pass

def get_str(prompt) -> str:
    pass

def get_date(prompt) -> datetime:
    pass

def get_bool(prompt) -> bool:
    pass
