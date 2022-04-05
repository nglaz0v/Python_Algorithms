# -*- coding: utf-8 -*-
"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция
нахождения простого числа должна принимать на вход натуральное и возвращать
соответствующее простое число. Проанализировать скорость и сложность
алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""


def eratosthenes_full(n):
    """Решето Эратосфена (нахождение всех простых чисел до заданного N)"""
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result


def sieve(k):
    """Нахождение k-го по счёту простого числа с помощью решета Эратосфена"""
    n = 100000
    sieve = [i * (i & 1) for i in range(n)]
    sieve[1] = 0
    sieve[2] = 2
    for i in range(3, n, 2):
        if sieve[i] != 0:
            for j in range(i * 2, n, i):
                sieve[j] = 0
    result = [i for i in sieve if i != 0]
    # print(result)
    return result[k]


def prime(k):
    """Нахождение k-го по счёту простого числа без помощи решета Эратосфена"""
    # TODO
    pass


def test_task(func):
    """Проверка: сравнение с эталонными значениями"""
    etalons = [2, 3, 5, 7]
    for i, item in enumerate(etalons):
        assert item == func(i)
        print(f"Test {item} OK")


# python3 -m timeit -n 1000 -s "from les_4_task_2 import eratosthenes" "eratosthenes(100000)"
# 1000 loops, best of 5: 26.5 msec per loop


if __name__ == "__main__":
    test_task(sieve)
    # test_task(prime)
    import cProfile
    cProfile.run("eratosthenes(100000)")
    # 1    0.035    0.035    0.043    0.043 les_4_task_2.py:15(eratosthenes)
