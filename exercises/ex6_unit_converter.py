from numbers import Number
from utils import validate_positive_numbers

####################################


class UnitConverter:
    def __init__(self, value: Number):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, n_value):
        # validation code for the new value
        validate_positive_numbers(n_value)

        self._value = n_value

    def inch_to_cm(self):
        return 2.54 * self.value

    def foot_to_meters(self):
        return .3048 * self.value

    def pound_to_kg(self):
        return 0.4535 * self.value


unit_converter = UnitConverter(5)


try:
    unit_converter.value = "d"
except TypeError as err:
    print(err)

try:
    unit_converter.value = -1
except ValueError as err:
    print(err)

print(f"{unit_converter.inch_to_cm()=}")
print(f"{unit_converter.foot_to_meters()=}")
print(f"{unit_converter.pound_to_kg()=}")
