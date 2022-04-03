# -*- coding: utf-8 -*-
"""
Сформировать из введённого числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""


def int_reverse(number):
    """Инвертировать порядок цифр натурального числа"""
    result = 0
    while (number > 0):
        digit = number % 10
        result *= 10
        result += digit
        number //= 10
    return result


print(__doc__)
number = int(input("N: "))
result = int_reverse(number)
print(f"X: {result}")
