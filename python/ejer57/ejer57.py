import numpy as np


def create_aleatory_array(start: int, stop: int) -> np.ndarray:
    array: np.ndarray = np.arange(start, stop)
    return array


def is_odd(arr: np.ndarray) -> list[int]:
    odd_list: list[int] = [odd for odd in arr if odd % 2 == 0]
    print(f"Los números pares de la lista son: {odd_list}")
    return odd_list


def vertical_concat(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.concatenate((arr1, arr2))  # sería lo mismo que utilizar vstack(arr1, arr2)


def horizontal_concat(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    new_arr: np.ndarray = np.hstack((arr1, arr2))
    return new_arr


print(create_aleatory_array(0, 10))
print(create_aleatory_array(1, 11))
is_odd(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print(f"Concatenación por defecto:\n{vertical_concat(a, b)}\n")
print(f"Concatenación con fusión de columnas:\n{horizontal_concat(a, b)}")
