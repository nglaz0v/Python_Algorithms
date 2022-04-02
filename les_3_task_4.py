# -*- coding: utf-8 -*-
"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

n = int(input("N: "))
k = int(input("K: "))
a = [random.randint(0, k) for i in range(n)]
print(a)

stat = {k: 0 for k in set(a)}
for x in a:
    stat[x] += 1
print(stat)

max_v = -k-1
for val in stat:
    if stat[val] > max_v:
        max_v = val
print(max_v)
