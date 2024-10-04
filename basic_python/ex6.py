def prime_factorization(num: int):
    dct = {}
    divider = 2

    while num > 1:
        while num % divider == 0:
            if divider in dct:
                dct[divider] += 1
            else:
                dct[divider] = 1
            num //= divider
        divider += 1

    s = ""
    for key, value in dct.items():
        if value == 1:
            s += f"({key})"
        else:
            s += f"({key}**{value})"
    return s


assert (prime_factorization(86240) ==
        "(2**5)(5)(7**2)(11)"), f"Ожидаемый ответ: (2**5)(5)(7**2)(11), Текущий ответ: {prime_factorization(86240)}"
assert prime_factorization(
    60) == "(2**2)(3)(5)", f"Ожидаемый ответ: (2**2)(3)(5), Текущий ответ: {prime_factorization(60)}"
assert prime_factorization(
    100) == "(2**2)(5**2)", f"Ожидаемый ответ: (2**2)(5**2), Текущий ответ: {prime_factorization(100)}"

print("Все тесты пройдены!")
