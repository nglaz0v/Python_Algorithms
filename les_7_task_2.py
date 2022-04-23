# -*- coding: utf-8 -*-
"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
"""

import random


def merge_sort(a, desc=False):
    """
    Сортировка методом слияния

    :param a: исходный массив
    :param desc: False - по возрастанию; True - по убыванию
    :return: отсортированный массив
    """
    lt = lambda a, b: a < b
    gt = lambda a, b: a > b
    cmp = gt if desc else lt
    if len(a) < 2:
        return a
    a_L = merge_sort(a[:len(a) // 2], desc)
    i_L = 0
    a_R = merge_sort(a[len(a) // 2:], desc)
    i_R = 0
    a_C = [0] * (len(a_L) + len(a_R))
    i_C = 0
    while i_L < len(a_L) and i_R < len(a_R):
        if cmp(a_L[i_L], a_R[i_R]):
            a_C[i_C] = a_L[i_L]
            i_L += 1
        else:
            a_C[i_C] = a_R[i_R]
            i_R += 1
        i_C += 1
    while i_L < len(a_L):
        a_C[i_C] = a_L[i_L]
        i_L += 1
        i_C += 1
    while i_R < len(a_R):
        a_C[i_C] = a_R[i_R]
        i_R += 1
        i_C += 1
    for i in range(len(a)):
        a[i] = a_C[i]
    return a


print(__doc__)
size = 12
array = [random.random()*50 for i in range(size)]
print(', '.join(f'{x:.2f}' for x in array))
merge_sort(array)
print(', '.join(f'{x:.2f}' for x in array))
