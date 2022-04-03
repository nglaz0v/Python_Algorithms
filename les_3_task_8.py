# -*- coding: utf-8 -*-
"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введённых элементов каждой строки и записывать
её в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

print(__doc__)
nrows = 5
ncols = 4

matrix = []  # [[None for _ in range(ncols)] for _ in range(nrows)]
for i in range(nrows):
    matrix.append([])
    s = 0
    for j in range(ncols-1):
        x = int(input(f"A[{i},{j}]: "))
        matrix[i].append(x)
        s += x
    matrix[i].append(s)

for line in matrix:
    for item in line:
        print(f"{item:>4}", end='')
    print()
