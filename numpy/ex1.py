import numpy as np


def sum_prod(X, V):
    result = np.zeros((X[0].shape[0], 1))
    for matrix, vector in zip(X, V):
        result += np.dot(matrix, vector)
    return result


X = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
V = [np.array([[9], [10]]), np.array([[3], [2]])]
expected_result = np.array([[56], [104]])
assert np.array_equal(sum_prod(X, V),
                      expected_result), f"Ожидаемый ответ: {expected_result}, Текущий ответ: {sum_prod(X, V)}"

X = [np.array([[1, 0, -5], [3, 2, -2], [4, 6, 0]]), np.array([[1, 1, 1], [2, -1, 0], [3, 5, -4]])]
V = [np.array([[2], [0], [-1]]), np.array([[1], [2], [3]])]
expected_result = np.array([[13], [8], [9]])
assert np.array_equal(sum_prod(X, V),
                      expected_result), f"Ожидаемый ответ: {expected_result}, Текущий ответ: {sum_prod(X, V)}"

print("Все тесты прошли успешно!")
