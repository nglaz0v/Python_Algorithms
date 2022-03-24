# -*- coding: utf-8 -*-
"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def digits_sum(number):
    s = 0
    while (number > 0):
        digit = number % 10
        s += digit
        number //= 10
    return s


n = int(input("N: "))
x = 0
for i in range(n):
    number = int(input(f"{i+1}: "))
    if (digits_sum(number) > digits_sum(x)):
        x = number
print(f"{x=} ({digits_sum(x)})")
