# Написать программу, которая генерирует в указанных пользователем границах:
#   a. случайное целое число,
#   b. случайное вещественное число,
#   c. случайный символ.
# Для каждого из трёх случаев пользователь задаёт свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти
# символы. Программа должна вывести на экран любой символ алфавита от 'a' до
# 'f' включительно.

import random

x = None
c = input("a - int; b - float; c - char: ").lower()
if (c == 'a'):
    a = int(input("A: "))
    b = int(input("B: "))
    if (a <= b):
        x = random.randint(a, b)
elif (c == 'b'):
    a = float(input("A: "))
    b = float(input("B: "))
    x = random.uniform(a, b)
elif (c == 'c'):
    a = input("A: ").lower()
    b = input("B: ").lower()
    if (ord(a) <= ord(b)):
        x = chr(random.randint(ord(a), ord(b)))
print(x)
