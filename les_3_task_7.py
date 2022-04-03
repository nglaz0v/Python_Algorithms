# -*- coding: utf-8 -*-
"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут
быть как равны между собой (оба минимальны), так и различаться.
"""

import random

print(__doc__)
n = int(input("Количество элементов массива: "))
k = int(input("Супремум массива: "))
a = [random.randint(-k, k) for i in range(n)]
print(a)

min_i = [0, 0]
min_v = [a[0], a[0]]
j = 0
for i in range(1, len(a)):
    if a[i] < min_v[j]:
        min_i[j], min_v[j] = i, a[i]
        j = (j + 1) % 2
print(f"#{min_i[0]}: {min_v[0]}; #{min_i[1]}: {min_v[1]}")
