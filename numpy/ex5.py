import numpy as np


def chess(m, n, a, b):
    if m == 0 and n == 0:
        return np.array([])

    mat = np.zeros((m, n), dtype=int)

    mat[::2, ::2] = a
    mat[1::2, 1::2] = a
    mat[::2, 1::2] = b
    mat[1::2, ::2] = b

    return mat


result = chess(2, 2, 1, 0)
expected = np.array([[1, 0], [0, 1]])
assert np.array_equal(result, expected), f"Ожидаемый ответ: {expected}, Текущий ответ: {result}"

result = chess(3, 3, 2, 5)
expected = np.array([[2, 5, 2], [5, 2, 5], [2, 5, 2]])
assert np.array_equal(result, expected), f"Ожидаемый ответ: {expected}, Текущий ответ: {result}"

result = chess(0, 0, 0, 1)
expected = np.array([])
assert np.array_equal(result, expected), f"Ожидаемый ответ: {expected}, Текущий ответ: {result}"

print("Все тесты пройдены!")
