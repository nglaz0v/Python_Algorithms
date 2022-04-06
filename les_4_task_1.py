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


def reverse_1(number):
    """Инвертировать порядок цифр натурального числа (числовая версия)"""
    result = 0
    while (number > 0):
        digit = number % 10
        result *= 10
        result += digit
        number //= 10
    return result


def reverse_2(number):
    """Инвертировать порядок цифр натурального числа (рекурсивная версия)"""
    def invert(number):
        if (len(number) == 1):
            return number
        else:
            return invert(number[1:]) + number[:1]
    return int(invert(str(number)))


def reverse_3(number):
    """Инвертировать порядок цифр натурального числа (версия со срезами)"""
    return int(str(number)[::-1])


def test_task(n):
    """Проверка: сравнение значений функций reverse() между собой"""
    a = reverse_1(n)
    b = reverse_2(n)
    c = reverse_3(n)
    print("%d : %d = %d = %d" % (n, a, b, c))
    assert a == b == c


# python3 -m timeit -n 1000 -s "from les_4_task_1 import reverse_1" "reverse_1(92233720368547758070)"
# 1000 loops, best of 5: 3.09 usec per loop
# python3 -m timeit -n 1000 -s "from les_4_task_1 import reverse_2" "reverse_2(92233720368547758070)"
# 1000 loops, best of 5: 5.32 usec per loop
# python3 -m timeit -n 1000 -s "from les_4_task_1 import reverse_3" "reverse_3(92233720368547758070)"
# 1000 loops, best of 5: 414 nsec per loop


if __name__ == "__main__":
    test_task(92233720368547758070)

#    import cProfile
#    cProfile.run("reverse_1(92233720368547758070)")
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(reverse_1)
#    cProfile.run("reverse_2(92233720368547758070)")
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(reverse_2)
#    cProfile.run("reverse_3(92233720368547758070)")
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(reverse_3)
