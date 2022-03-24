# -*- coding: utf-8 -*-
"""
Посчитать чётные и нечётные цифры введённого натурального числа. Например, если
введено число 34560, в нём 3 чётные цифры (4, 6 и 0) и 2 нечётные (3 и 5).
"""


def count_even_odd(number):
    """Посчитать чётные и нечётные цифры натурального числа"""
    even = 0
    odd = 0
    while (number > 0):
        digit = number % 10
        # print(f"{digit}")
        if ((digit % 2) == 0):
            even += 1
        else:
            odd += 1
        number //= 10
    return even, odd


number = int(input("N: "))
even, odd = count_even_odd(number)
print(f"чётных: {even}, нечётных: {odd}")
