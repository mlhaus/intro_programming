from ui_helpers import show_section_title
from user_input import get_str, get_date, get_int, get_bool, get_float
from table import print_table
import copy

'''
This module contains functions related to creating, reading, updating, and deleting baseball team records
'''

teams = []


def add_team():
    """
    Handles logic for adding one employee record
    INPUTS: None
    OUTPUT: None
    """
    get_team_data()
    get_all_teams()


def get_team_data() -> None:
    """
    Prompt the user for the employee's name (first, last), dob, dependents, extra withholding
    INPUTS: None
    OUTPUT: None
    """
    list = []
    # prompt the user for strings, floats, ints, dates, bools
    teams.append(list)


def get_all_teams():
    """
    Handles logic for getting all employee records
    INPUTS: None
    OUTPUT: None
    """
    # Replace header strings with your column headings
    header = []
    copy_teams = copy.deepcopy(teams)
    copy_teams.insert(0, header)
    print_table(copy_teams)


def get_team():
    """
    Handles logic for getting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass


def update_team():
    """
    Handles logic for updating one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass


def delete_team():
    """
    Handles logic for deleting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass