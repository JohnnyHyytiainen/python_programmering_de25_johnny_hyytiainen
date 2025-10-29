from pytest import raises, approx
from vector import Vector


def test_valid_init():
    v = Vector(1, 2)
    assert v.numbers == (1, 2)

# Test negative values in init


def test_negative_init():
    v = Vector(-1, -15, 3)
    assert v.numbers == (-1, -15, 3)


# Test string in the init
def test_string_init_fails():
    with raises(TypeError):
        Vector("1")


# test len() function
def test_length_init():
    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3)
    v3 = Vector(1, 3, 2)
    assert len(v1) != len(v2)
    assert len(v3) == len(v1)

    vectors = (Vector(1, 2), Vector(1), Vector(1, 2, 3), Vector(1, 4, 2, 3))
    expected_lenghts = (2, 1, 3, 4)
    for a, b in zip(vectors, expected_lenghts):
        assert len(a) == b


# test abs() function
def test_vector_norm_valid():
    v = Vector(1, 4)
    expected_norm = (v[0]**2 + v[1]**2)**.5

    assert abs(v) == approx(expected_norm)
    assert abs(v) != approx(4.12)


# def test_absolute_init():


def test_empty_vector_fail() -> None:
    with raises(ValueError):
        Vector()
