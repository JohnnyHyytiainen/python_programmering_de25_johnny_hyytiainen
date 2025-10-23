from numbers import Number


def validate_number(number):
    if not isinstance(number, Number):
        raise TypeError(f"elements/value must be numbers not {type(number)}")
