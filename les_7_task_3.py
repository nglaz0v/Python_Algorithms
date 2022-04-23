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
m = 7
size = 2*m+1
array = [i for i in range(size)]
random.shuffle(array)
print(array)

below = {min(array[0], array[1], array[2])}
above = {max(array[0], array[1], array[2])}
for i in range(0, len(array)):
    # print(f"{array[i]=}: {below=} {above=}")
    if (array[i] < max(below)):
        below.add(array[i])
    elif (array[i] > min(above)):
        above.add(array[i])
    else:
        below.add(array[i])
        above.add(array[i])
    if (len(below) > (len(above)+1)):
        above.add(max(below))
        below.remove(max(below))
    elif (len(above) > (len(below)+1)):
        below.add(min(above))
        above.remove(min(above))
# print(sorted(below))
# print(sorted(above))

median = None
if len(below) < len(above):
    median = min(above)
elif len(below) > len(above):
    median = max(below)
else:
    median = (below & above).pop()
assert median == sorted(array)[m]
print(f"{median = }")
