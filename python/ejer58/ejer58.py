import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.array([2, 6, 1, 9, 10, 3, 27])
d = np.array([5, 7, 9, 8, 6, 4, 5])
e = np.array([6, 3, 4, 8, 9, 7, 1])


def is_equal(arr1: np.ndarray, arr2: np.ndarray) -> list[int]:
    numbers_bool = np.equal(arr1, arr2)
    equal_numbers = arr1[numbers_bool]
    return equal_numbers


def found_values(arr: np.ndarray, first: int, second: int) -> list[int]:
    num_val = [num for num in arr if first <= num <= second]
    return num_val


def maxx(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


print(is_equal(a, b))
print(found_values(c, 5, 10))

print(np.frompyfunc(maxx, 2, 1)(d, e))

iris_df: pd.DataFrame = pd.read_csv("iris.data", header=None)
iris_df.columns = pd.Index(['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
arr_sepal: np.ndarray = np.array(iris_df['sepal length'].values)
normalized: np.ndarray = np.round((arr_sepal - min(arr_sepal)) / (max(arr_sepal) - min(arr_sepal)), decimals=3)
print(normalized)

