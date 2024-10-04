def is_balanced(num: int):
    lst = [int(i) for i in str(num)]
    len_lst = len(lst)

    if len_lst % 2 == 0:
        if sum(lst[:len_lst // 2 - 1]) == sum(lst[len_lst // 2 + 1:]):
            return True
        return False
    else:
        if sum(lst[:len_lst // 2]) == sum(lst[len_lst // 2 + 1:]):
            return True
        return False


assert is_balanced(12521) is True, f"Ожидаемый ответ: True, Текущий ответ: {is_balanced(12521)}"
assert is_balanced(10) is True, f"Ожидаемый ответ: True, Текущий ответ: {is_balanced(10)}"
assert is_balanced(5) is True, f"Ожидаемый ответ: True, Текущий ответ: {is_balanced(5)}"
assert is_balanced(127568) is False, f"Ожидаемый ответ: False, Текущий ответ: {is_balanced(127568)}"
assert is_balanced(12345231) is True, f"Ожидаемый ответ: True, Текущий ответ: {is_balanced(12345231)}"

print("Все тесты пройдены!")
