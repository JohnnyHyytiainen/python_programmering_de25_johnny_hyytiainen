from pytest import raises
from triangle import Triangle


def test_valid_init():
    triangle = Triangle(base=5, height=2)
    assert triangle.base == 5 and triangle.height == 2


def test_ngative_base_fail():
    with raises(ValueError):
        Triangle(base=-1, height=2)


def test_ngative_hieght_fail():
    with raises(ValueError):
        Triangle(base=2, height=-1)


def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Triangle(base="1", height=1)


def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Triangle(base=1, height=True)


def test_zero_base_fail():
    with raises(ValueError):
        Triangle(base=0, height=1)


def test_area_calculation():
    triangle = Triangle(base=2, height=3)
    assert triangle.area == 3


def test_valid_init():
    triangle = Triangle(base=5, height=2)
    assert triangle.base == 5 and triangle.height == 2


def test_ngative_base_fail():
    with raises(ValueError):
        Triangle(base=-1, height=2)


def test_ngative_hieght_fail():
    with raises(ValueError):
        Triangle(base=2, height=-1)


def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Triangle(base="1", height=1)


def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Triangle(base=1, height=True)


def test_zero_base_fail():
    with raises(ValueError):
        Triangle(base=0, height=1)


def test_area_calculation():
    triangle = Triangle(base=2, height=3)
    assert triangle.area == 3
