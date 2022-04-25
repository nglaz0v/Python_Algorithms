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

below = [min(array)]  # "нижние" элементы (которые меньше медианы)
above = [max(array)]  # "верхние" элементы (которые больше медианы)
for i in range(0, len(array)):
    # print(f"{array[i]=}: {below=} {above=}")
    if (array[i] <= max(below)):  # очередной элемент меньше максимума из "нижних"
        below.append(array[i])  # добавить его к "нижним"
    elif (array[i] >= min(above)):  # очередной элемент больше минимума из "верхних"
        above.append(array[i])  # добавить его к "верхним"
    else:
        # добавить чётные к "нижним", а нечётные - к "верхним"
        # (распределятся сами в ходе балансировки)
        if (i % 2 == 0):
            below.append(array[i])
        else:
            above.append(array[i])
    # количество "нижних" и "верхних" элементов должно быть сбалансировано
    # (не должно различаться более чем на 1)
    if (len(below) >= (len(above)+1)):
        # максимум из "нижних" отправить к "верхним"
        above.append(max(below))
        below.remove(max(below))
    elif (len(above) >= (len(below)+1)):
        # минимум из "верхних" отправить к "нижним"
        below.append(min(above))
        above.remove(min(above))
below.remove(min(array))  # удалить лишний элемент из списка "нижних"
above.remove(max(array))  # удалить лишний элемент из списка "верхних"
# print(sorted(below), len(below))
# print(sorted(above), len(above))
# print(sorted(array), len(array))
# print(sorted(below+above), len(below+above))

median = None
if len(below) < len(above):
    median = min(above)  # минимум из "верхних"
elif len(below) > len(above):
    median = max(below)  # максимум из "нижних"
assert median == sorted(array)[m]
print(f"{median = }")
