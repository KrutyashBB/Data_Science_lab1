def count_positive_bits(num: int):
    result = 0
    while num > 0:
        if num % 2 != 0:
            num = (num - 1) // 2
            result += 1
            continue
        num //= 2
    return result
    # или использовать bin() + count


assert count_positive_bits(0) == 0, f"Ожидаемый ответ: 0, Текущий ответ: {count_positive_bits(0)}"
assert count_positive_bits(1) == 1, f"Ожидаемый ответ: 1, Текущий ответ: {count_positive_bits(1)}"
assert count_positive_bits(2) == 1, f"Ожидаемый ответ: 1, Текущий ответ: {count_positive_bits(2)}"
assert count_positive_bits(3) == 2, f"Ожидаемый ответ: 2, Текущий ответ: {count_positive_bits(3)}"
assert count_positive_bits(7) == 3, f"Ожидаемый ответ: 3, Текущий ответ: {count_positive_bits(7)}"
assert count_positive_bits(15) == 4, f"Ожидаемый ответ: 4, Текущий ответ: {count_positive_bits(15)}"
assert count_positive_bits(16) == 1, f"Ожидаемый ответ: 1, Текущий ответ: {count_positive_bits(16)}"
assert count_positive_bits(31) == 5, f"Ожидаемый ответ: 5, Текущий ответ: {count_positive_bits(31)}"

print("Все тесты пройдены!")
