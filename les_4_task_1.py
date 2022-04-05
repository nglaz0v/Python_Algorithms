# -*- coding: utf-8 -*-
"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трёх уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
   (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

# from les_2_task_2 import count_even_odd
# from les_2_task_3 import int_reverse
# from les_2_task_8 import count_digit
# from les_2_task_9 import digits_sum


def task(n):
    for i in range(n):
        x = i**i


# python3 -m timeit -n 1000 -s "from les_4_task_1 import task" "task(100)"
# 1000 loops, best of 5: 35.6 usec per loop


if __name__ == "__main__":
    import cProfile
    cProfile.run("task(100)")
    # 1    0.000    0.000    0.000    0.000 les_4_task_1.py:23(task)
