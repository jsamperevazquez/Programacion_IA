import numpy as np
from ejer57 import create_aleatory_array, is_odd, horizontal_concat


def test_is_odd():
    assert [0, 2, 4] == is_odd(np.arange(6))


def test_create_aleatory_array():
    assert 9 == create_aleatory_array(0, 10)[-1]
    assert 8 == create_aleatory_array(0, 10)[-2]


def test_horizontal_concat():
    a = np.array([1, 2])
    b = np.array([3, 4])
    result = np.array([1, 2, 3, 4])
    assert np.array_equal(result, horizontal_concat(a, b))

