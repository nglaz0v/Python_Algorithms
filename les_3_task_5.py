# -*- coding: utf-8 -*-
"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его
значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный
отрицательный». Это два абсолютно разных значения.
"""

import random

n = int(input("N: "))
k = int(input("K: "))
a = [random.randint(-k, k) for i in range(n)]
print(a)

max_neg_i, max_neg_v = 0, -k
for i in range(len(a)):
    if (a[i] < 0) and (a[i] > max_neg_v):
        max_neg_i, max_neg_v = i, a[i]
print(f"{max_neg_i}: {max_neg_v}")
