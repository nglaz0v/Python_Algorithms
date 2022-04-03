# -*- coding: utf-8 -*-
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

print(__doc__)
k = int(input("Супремум матрицы: "))
nrows = int(input("Количество строк матрицы: "))
ncols = int(input("Количество столбцов матрицы: "))

matrix = [[random.randint(-k, k) for _ in range(ncols)] for _ in range(nrows)]
for line in matrix:
    for item in line:
        print(f"{item:>4}", end='')
    print()

maxj = -k-1
for j in range(ncols):
    mini = matrix[0][j]
    for i in range(nrows):
        if matrix[i][j] < mini:
            mini = matrix[i][j]
    if mini > maxj:
        maxj = mini
print(f"{maxj}")
