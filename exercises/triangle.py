from numbers import Number


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
        pass

    # @property
    # def perimeter(self):
        # pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __repr__(self):
        pass
