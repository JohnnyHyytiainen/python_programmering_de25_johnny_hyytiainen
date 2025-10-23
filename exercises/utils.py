from numbers import Number


def validate_positive_numbers(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(
            f"The value must be a Number not a {type(value)}")

    if value < 0:
        raise ValueError(f"Value cant be a negatie value {value}")
