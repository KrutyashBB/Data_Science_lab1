def is_has_duplicate(string: str):
    return len(set(string)) != len(string)


assert is_has_duplicate("abbc") is True, f"Ожидаемый ответ: True, Текущий ответ: {is_has_duplicate('abbc')}"
assert is_has_duplicate("abcd") is False, f"Ожидаемый ответ: False, Текущий ответ: {is_has_duplicate('abcd')}"
assert is_has_duplicate("Aa") is False, f"Ожидаемый ответ: False, Текущий ответ: {is_has_duplicate('Aa')}"
assert is_has_duplicate("") is False, f"Ожидаемый ответ: False, Текущий ответ: {is_has_duplicate('')}"
assert is_has_duplicate("abc!@") is False, f"Ожидаемый ответ: False, Текущий ответ: {is_has_duplicate('abc!@')}"
assert is_has_duplicate("abbCCCc") is True, f"Ожидаемый ответ: True, Текущий ответ: {is_has_duplicate('abbCCCc')}"

print("Все тесты прошли успешно!")
