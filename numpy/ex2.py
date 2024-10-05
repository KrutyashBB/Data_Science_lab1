import numpy as np


def unique_rows(mat):
    return [np.unique(row).tolist() for row in mat]


def unique_columns(mat):
    if len(np.shape(mat)) == 1:
        return []
    return [np.unique(mat[:, indCol]).tolist() for indCol in range(np.shape(mat)[1])]


mat = np.array([[1, 2, 3], [1, 1, 1]])
expectedRow = [[1, 2, 3], [1]]
expectedCol = [[1], [1, 2], [1, 3]]

assert unique_rows(mat) == expectedRow, f"Ожидаемый ответ: {expectedRow}, Текущий ответ: {unique_rows(mat)}"
assert unique_columns(mat) == expectedCol, f"Ожидаемый ответ: {expectedCol}, Текущий ответ: {unique_columns(mat)}"
assert unique_rows(np.array([])) == [], f"Ожидаемый ответ: {[]}, Текущий ответ: {unique_rows(np.array([]))}"
assert unique_columns(np.array([])) == [], f"Ожидаемый ответ: {[]}, Текущий ответ: {unique_columns(np.array([]))}"

print("Все тесты пройдены!")
