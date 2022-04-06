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

import math


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
    nums = [i * (i & 1) for i in range(n)]  # список для решета
                                            # (сразу обнулить все чётные числа)
    nums[1] = 0  # 1 - не простое число
    nums[2] = 2  # 2 - простое число
    for i in range(3, int(math.sqrt(n)), 2):
        if nums[i] != 0:
            for j in range(i ** 2, n, i):
                nums[j] = 0  # это не простое число
    q = -1
    for i in nums:
        if i != 0:
            q += 1
            if q == k:
                break
    return i


def prime(k):
    """Нахождение k-го по счёту простого числа без помощи решета Эратосфена"""

    def isprime(m):
        """Проверка, является ли число m простым"""
        if m == 2:
            return True  # 2 - простое число
        if m % 2 == 0:
            return False  # все чётные числа - не простые
        for i in range(3, int(math.sqrt(m))+1, 2):
            if m % i == 0:  # если i является делителем для m
                return False  # то это не простое число
        return True  # у m нет нетривиальных делителей - это простое число

    if k == 0:
        return 2
    n = 100000
    q = 0
    for i in range(3, n, 2):
        if isprime(i):
            q += 1
            if q == k:
                break
    return i


def test_task(func):
    """Проверка: сравнение с эталонными значениями"""
    etalons = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
               61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
               131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
               197, 199)
    for i, item in enumerate(etalons):
        print(f"[{func.__name__}] {i}: {item} = {func(i)}")
        assert item == func(i)


# python3 -m timeit -n 1000 -s "from les_4_task_2 import eratosthenes" "eratosthenes(100000)"
# 1000 loops, best of 5: 26.5 msec per loop


if __name__ == "__main__":
    test_task(sieve)
    test_task(prime)
#    import cProfile
#    cProfile.run("eratosthenes(100000)")
    # 1    0.035    0.035    0.043    0.043 les_4_task_2.py:15(eratosthenes)
