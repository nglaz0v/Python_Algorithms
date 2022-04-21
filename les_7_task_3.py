# -*- coding: utf-8 -*-
"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой —
не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это
слишком сложно, используйте метод сортировки, который не рассматривался на
уроках (сортировка слиянием также недопустима).
"""

import random

print(__doc__)
m = 5
size = 2*m+1
array = [i for i in range(size)]
random.shuffle(array)
print(array)
# ...
a = array[0]
b = array[1]
c = array[2]
lo = min(min(a, b), c)
hi = max(max(a, b), c)
med = (a + b + c) - lo - hi
#for i in range(1, len(array)-1):
#    a = min(array[i], array[i+1])
#    b = max(array[i], array[i+1])
#    lo = a if a < lo else lo
#    hi = b if b > hi else hi
#    tmp = sorted([max(a, lo), med, min(b,hi)])
#    med = tmp[1]
#    print(f"{a=}, {b=}, {lo=}, {hi=}, {med=}")
#    # lo = min(min(a, lo), med)
#    # hi = max(max(hi, b), med)
#    # med = (a + b + med) - lo - hi
aa = {min(a, b, c)}
bb = {max(a, b, c)}
for i in range(0, len(array)):
    print(f"{array[i]=}: {aa=} {bb=}")
    if array[i] < min(aa):
        aa.add(array[i])
    elif array[i] > max(bb):
        bb.add(array[i])
    elif (array[i] < max(aa)):
        aa.add(array[i])
    elif (array[i] > min(bb)):
        bb.add(array[i])
    else:
        aa.add(array[i])
        bb.add(array[i])
    if (len(aa) > (len(bb)+1)):
        bb.add(max(aa))
        aa.remove(max(aa))
    elif (len(bb)  > (len(aa)+1)):
        aa.add(min(bb))
        bb.remove(min(bb))
    # za = max(aa)
    # zb = min(bb)
    # if (za > zb):
    #    pass
print(sorted(aa))
print(sorted(bb))

import numpy as np
print(np.median(np.array(array)))
print(sorted(array)[m])
