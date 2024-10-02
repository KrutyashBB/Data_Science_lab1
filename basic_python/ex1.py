def count_vowel_letters(string: str):
    string = string.lower()
    result = 0
    for letter in string:
        if letter in "aeiou":
            result += 1
    return result


assert count_vowel_letters("abbc") == 1, f"Ожидаемый ответ: 1, Текущий ответ: {count_vowel_letters('abbc')}"
assert count_vowel_letters("") == 0, f"Ожидаемый ответ: 0, Текущий ответ: {count_vowel_letters('')}"
assert count_vowel_letters("bbc") == 0, f"Ожидаемый ответ: 0, Текущий ответ: {count_vowel_letters('bbc')}"
assert count_vowel_letters("aaa") == 3, f"Ожидаемый ответ: 3, Текущий ответ: {count_vowel_letters('aaa')}"
assert count_vowel_letters("aeiiou") == 6, f"Ожидаемый ответ: 6, Текущий ответ: {count_vowel_letters('aeiiou')}"
assert count_vowel_letters("AaEEiUu") == 7, f"Ожидаемый ответ: 7, Текущий ответ: {count_vowel_letters('AaEEiUu')}"

print("Все тесты прошли успешно!")
