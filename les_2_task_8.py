# -*- coding: utf-8 -*-
"""
Посчитать, сколько раз встречается определённая цифра в введённой
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.
"""


def count_digit(num, dgt):
    """Подсчитать, сколько раз цифра встречается в записи натурального числа"""
    count = 0
    while (num > 0):
        digit = num % 10
        if digit == dgt:
            count += 1
        num //= 10
    return count


n = int(input("N: "))
digit = int(input("d: "))
count = 0
for i in range(n):
    number = int(input(f"{i+1}: "))
    count += count_digit(number, digit)
print(f"{count=}")
