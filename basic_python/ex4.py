def magic(n: int):
    result = 0
    while n > 9:
        a = 1
        while n != 0:
            a *= n % 10
            n //= 10
        n = a
        result += 1
    return result


assert magic(39) == 3, f"Ожидаемый ответ: 3, Текущий ответ: {magic(39)}"
assert magic(4) == 0, f"Ожидаемый ответ: 0, Текущий ответ: {magic(4)}"
assert magic(999) == 4, f"Ожидаемый ответ: 4, Текущий ответ: {magic(999)}"
assert magic(10) == 1, f"Ожидаемый ответ: 1, Текущий ответ: {magic(10)}"
assert magic(77) == 4, f"Ожидаемый ответ: 4, Текущий ответ: {magic(77)}"

print("Все тесты пройдены!")
