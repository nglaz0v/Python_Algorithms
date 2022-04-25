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
m = int(input("m: "))
size = 2*m+1
array = [i for i in range(size)]
random.shuffle(array)
print(array)

below = {array[0]}  # "нижние" элементы (которые меньше медианы)
above = {array[0]}  # "верхние" элементы (которые больше медианы)
for i in range(1, len(array)):
    # print(f"{array[i]=}: {below=} {above=}")
    if (array[i] < max(below)):  # очередной элемент меньше максимума из "нижних"
        below.add(array[i])  # добавить его к "нижним"
    elif (array[i] > min(above)):  # очередной элемент больше минимума из "верхних"
        above.add(array[i])  # добавить его к "верхним"
    else:
        # добавить к обоим множествам
        below.add(array[i])
        above.add(array[i])
    # количество "нижних" и "верхних" элементов не должно различаться более чем на 1
    if (len(below) > (len(above)+1)):
        # максимум из "нижних" отправить к "верхним"
        above.add(max(below))
        below.remove(max(below))
    elif (len(above) > (len(below)+1)):
        # минимум из "верхних" отправить к "нижним"
        below.add(min(above))
        above.remove(min(above))
# print(sorted(below))
# print(sorted(above))

median = None
if len(below) < len(above):
    median = min(above)  # минимум из "верхних"
elif len(below) > len(above):
    median = max(below)  # максимум из "нижних"
else:
    median = (below & above).pop()  # пересечение "нижних" и "верхних" множеств
assert median == sorted(array)[m]
print(f"{median = }")
