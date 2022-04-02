# -*- coding: utf-8 -*-
"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут
быть как равны между собой (оба минимальны), так и различаться.
"""

import random

n = int(input("N: "))
k = int(input("K: "))
a = [random.randint(-k, k) for i in range(n)]
print(a)

min_i = [0, 0]
min_v = [a[0], a[0]]
q = 0
for i in range(1, len(a)):
    if a[i] < min_v[q]:
        min_i[q], min_v[q] = i, a[i]
        q = (q + 1) % 2
print(f"{min_i}: {min_v}")
