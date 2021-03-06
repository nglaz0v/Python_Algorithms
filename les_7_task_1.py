# -*- coding: utf-8 -*-
"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход
массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
шейкерная и другие в зачёт не идут.
"""

import random


def bubble_sort(a, desc=True):
    """
    Сортировка методом пузырька

    :param a: исходный массив
    :param desc: False - по возрастанию; True - по убыванию
    :return: отсортированный массив
    """
    lt = lambda a, b: a < b
    gt = lambda a, b: a > b
    cmp = lt if desc else gt
    N = len(a)
    for j in range(1, N):
        flag = False  # был ли хотя бы один обмен значениями
        for i in range(N - j):
            if cmp(a[i], a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                flag = True
        if not flag:
            break  # обменов не было -> массив уже отсортирован
        # print(a)
    return a


print(__doc__)
size = int(input("N: "))
array = [random.randint(-100, 100) for i in range(size)]
print(array)
bubble_sort(array)
print(array)
