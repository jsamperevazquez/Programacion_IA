import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.array([2, 6, 1, 9, 10, 3, 27])


def is_equal(arr1: np.ndarray, arr2: np.ndarray) -> list[int]:
    numbers_bool = np.equal(arr1, arr2)
    equal_numbers = arr1[numbers_bool]
    return equal_numbers


def found_values(arr: np.ndarray, first: int, second: int) -> list[int]:
    num_val = [num for num in arr if first <= num <= second]
    return num_val


def vector_arrays(a, b):
    pass


print(is_equal(a, b))
print(found_values(c, 5, 10))
