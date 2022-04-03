# -*- coding: utf-8 -*-
"""
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""

import random

print(__doc__)
n = int(input("Количество элементов массива: "))
k = int(input("Супремум массива: "))
a = [random.randint(-k, k) for i in range(n)]
print(a)

min_i, max_i = 0, 0
min_v, max_v = a[0], a[0]
for i in range(1, len(a)):
    if a[i] < min_v:
        min_i, min_v = i, a[i]
    if a[i] > max_v:
        max_i, max_v = i, a[i]
print(f"min #{min_i}: {min_v}; max #{max_i}: {max_v}")

a[min_i], a[max_i] = a[max_i], a[min_i]
print(a)
