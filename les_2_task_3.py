# -*- coding: utf-8 -*-
"""
Сформировать из введённого числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""

number = int(input("N: "))
result = 0
while (number > 0):
    digit = number % 10
    result *= 10
    result += digit
    number //= 10
print(f"X: {result}")
