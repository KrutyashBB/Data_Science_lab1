import numpy as np


def binarize(M, threshold=0.5):
    if M.size == 0:
        return []
    return (M > threshold).astype(int).tolist()


mat1 = np.array([])
mat2 = np.array([[1, 2, 3], [-2, 0, 3]])

assert binarize(mat1) == [], f"Ожидаемый ответ: {[]}, Текущий ответ: {binarize(mat1)}"
assert binarize(mat2) == [[1, 1, 1],
                          [0, 0, 1]], f"Ожидаемый ответ: {[[1, 1, 1], [0, 0, 1]]}, Текущий ответ: {binarize(mat2)}"
assert binarize(mat2, 1) == [[0, 1, 1], [0, 0, 1]], (f"Ожидаемый ответ: {[[0, 1, 1], [0, 0, 1]]}"
                                                     f", Текущий ответ: {binarize(mat2, 1)}")

print("Все тесты пройдены!")
