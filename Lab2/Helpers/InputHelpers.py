from datetime import datetime

from Helpers.DataTypeHelpers import *
__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']


def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): ") -> str:
    value_error_msg = f"Value must be a date"
    while True:
        try:
            user_input = input(prompt)
            if not isDate(user_input):
                raise ValueError(value_error_msg)
        except ValueError as e:
            print(e)
            continue  # Continue the while loop until no exception

        return datetime.datetime.fromisoformat(user_input)


def inputInt(prompt: str = "Enter an integer: ", min_value: int = 0, max_value: int = 100) -> str:
    value_error_msg = f"Value must be between {min_value} and {max_value}"
    while True:
        try:
            user_input = input(prompt)
            if not isInt(user_input):
                raise ValueError(value_error_msg)
            if int(user_input) < min_value:
                raise ValueError(value_error_msg)
            if int(user_input) > max_value:
                raise ValueError(value_error_msg)
        except ValueError as e:
            print(e)
            continue  # Continue the while loop until no exception

        return str(user_input)


def inputFloat(prompt: str = "Enter a float: ", min_value: float = 0, max_value: float = 100) -> str:
    value_error_msg = f"Value must be between {min_value} and {max_value}"
    while True:
        try:
            user_input = input(prompt)
            if not isFloat(user_input):
                raise ValueError(value_error_msg)
            if float(user_input) < min_value:
                raise ValueError(value_error_msg)
            if float(user_input) > max_value:
                raise ValueError(value_error_msg)

        except ValueError as e:
            print(e)
            continue  # Continue the while loop until no exception

        return str(user_input)


def inputString(prompt: str = "Enter a string: ", min_length: int = 0, max_length: int = 100) -> str:
    value_error_msg = f"Text must be between {min_length} and {max_length} in length"
    while True:
        try:
            user_input = input(prompt)
            if len(user_input) < min_length:
                raise ValueError(value_error_msg)
            if len(user_input) > max_length:
                raise ValueError(value_error_msg)

        except ValueError as e:
            print(e)
            continue  # Continue the while loop until no exception
        return str(user_input)
