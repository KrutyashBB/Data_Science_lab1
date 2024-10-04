def pyramid(number: int):
    if number < 1:
        return "It is impossible"

    a = 1
    sum_squares = 0
    last_num = 0
    while sum_squares < number:
        sum_squares += a ** 2
        last_num = a
        a += 1
    if sum_squares == number:
        return last_num
    else:
        return "It is impossible"


assert pyramid(5) == 2, f"Ожидаемый ответ: 2, Текущий ответ: {pyramid(5)}"
assert pyramid(-2) == "It is impossible", f"Ожидаемый ответ: It is impossible, Текущий ответ: {pyramid(-2)}"
assert pyramid(14) == 3, f"Ожидаемый ответ: 3, Текущий ответ: {pyramid(14)}"
assert pyramid(1) == 1, f"Ожидаемый ответ: 1, Текущий ответ: {pyramid(1)}"

print("Все тесты прошли успешно!")
