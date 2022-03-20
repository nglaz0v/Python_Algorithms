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
c = input("a - int; b - float; c - char: ")[0].lower()
if (c == 'a'):
    a = int(input("a: "))
    b = int(input("b: "))
    if (a <= b):
        x = random.randint(a, b)
elif (c == 'b'):
    a = float(input("a: "))
    b = float(input("b: "))
    x = random.uniform(a, b)
elif (c == 'c'):
    a = input("a: ")[0].lower()
    b = input("b: ")[0].lower()
    if (ord(a) <= ord(b)):
        x = chr(random.randint(ord(a), ord(b)))
print(x)
