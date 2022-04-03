# -*- coding: utf-8 -*-
"""
Написать программу, которая генерирует в указанных пользователем границах:
    a. случайное целое число,
    b. случайное вещественное число,
    c. случайный символ.
Для каждого из трёх случаев пользователь задаёт свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти
символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.
"""

import random

print(__doc__)
x = None
c = input("a - int; b - float; c - char: ").lower()
a = input("A: ")
b = input("B: ")
if (c == 'a'):
    a = int(a)
    b = int(b)
    if (a <= b):
        x = random.randint(a, b)
elif (c == 'b'):
    a = float(a)
    b = float(b)
    x = random.uniform(a, b)
elif (c == 'c'):
    a = ord(a.lower())
    b = ord(b.lower())
    if (a <= b):
        x = chr(random.randint(a, b))
print(x)
