from numbers import Number
from functools import total_ordering
from math import sqrt


@total_ordering
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"{value} must be a number")
        if value <= 0:
            raise ValueError("Base must be positive")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"{value} must be a number")
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return (self._base * self._height) / 2  # Fixad: ingen rekursion!

    # Exempel på perimeter (om det är en rätvinklig triangel)
    @property
    def perimeter(self):
        hypotenuse = sqrt(self._base**2 + self._height**2)
        return self._base + self._height + hypotenuse

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return False
        return self.area == other.area  # Jämför baserat på area

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError("Cannot compare Triangle with non-Triangle")
        return self.area < other.area  # För sortering baserat på area

    def __repr__(self):
        return f"Triangle(base={self._base}, height={self._height})"

    # Onödig med total_ordering för att använda
    # __le__, __gt__, __ge__


trajangle = Triangle(base=13, height=10)

print(trajangle.area)
