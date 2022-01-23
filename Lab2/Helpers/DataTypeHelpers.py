import datetime
__all__ = ['isInt', 'isFloat', 'isDate']


def isInt(value: str) -> bool:
    """
    This function accepts a string value and returns True if that value can be parsed to an int data type, False otherwise
    :param value:
    :return: True if param "value" can be parsed into an int data type, False otherwise
    """
    try:
        int(value)
    except Exception:
        return False

    return True


def isFloat(value: str) -> bool:
    """
    This function accepts a string value and returns True if that value can be parsed to a float data type, False otherwise.
    :param value:
    :return: True if the param "value" can be parsed to a float data type, False otherwise.
    """
    try:
        float(value)
    except Exception:
        return False

    return True


def isDate(value: str) -> bool:
    """
    This function accepts a string value and returns True if that value can be parsed to a datetime
    data type in ISO serialization format (yyyy-mm-dd), False otherwise.
    :param value:
    :return: True param "value" can be parsed to a datetime data type in ISO serialization format (yyyy-mm-dd), False otherwise.
    """
    try:
        datetime.datetime.fromisoformat(value)
    except Exception:
        return False

    return True