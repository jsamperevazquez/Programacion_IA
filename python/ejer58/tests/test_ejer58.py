import numpy as np
from ejer58 import is_equal, found_values

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([0, 2, 2, 4, 9, 8, 7, 6, 5])
equal = [2, 4, 7]
values_between = [3, 4, 5]


def test_is_equal():
    assert np.array_equal(equal, is_equal(a, b))


def test_found_values():
    assert np.array_equal(values_between, found_values(a, 3, 5))
