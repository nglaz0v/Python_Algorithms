# -*- coding: utf-8 -*-
"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

print(__doc__)
n = int(input("Количество элементов массива: "))
k = int(input("Супремум массива: "))
a = [random.randint(0, k) for i in range(n)]
print(a)

stat = {k: 0 for k in set(a)}
for x in a:
    stat[x] += 1
print(stat)

max_c, max_v = -1, -k-1
for val in stat:
    if stat[val] > max_c:
        max_v, max_c = val, stat[val]
print(f"Чаще всего в массиве встречается число {max_v} ({stat[max_v]} раз)")
