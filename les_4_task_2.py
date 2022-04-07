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

# def eratosthenes(n):
#    """Решето Эратосфена (нахождение всех простых чисел до заданного N)"""
#    sieve = [i for i in range(n)]
#    sieve[1] = 0
#    for i in range(2, n):
#        if sieve[i] != 0:
#            j = i * 2
#            while j < n:
#                sieve[j] = 0
#                j += i
#    result = [i for i in sieve if i != 0]
#    return result


def sieve(k: int) -> int:
    """Нахождение k-го по счёту простого числа с помощью решета Эратосфена"""
    n = 10**6
    nums = [i * (i & 1) for i in range(n)]  # список для решета
                                            # (сразу обнулить все чётные числа)
    nums[1] = 0  # 1 - не простое число
    nums[2] = 2  # 2 - простое число
    for i in range(3, int(n**(1/2))+1, 2):
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


def isprime(n: int) -> bool:
    """Проверка, является ли число n простым"""
    if n <= 3:
        return n > 1  # 2 и 3 - простые числа
    if not (n % 2) or not (n % 3):
        return False  # все числа, кратные 2 или 3 - не простые
    for i in range(5, int(n**0.5)+1, 6):
        if not (n % i) or not (n % (i + 2)):
            # числа i+1, i+3, i+4, i+5 гарантировано делятся либо на 2 либо на 3
            return False  # то это не простое число
    return True  # у m нет нетривиальных делителей - это простое число


def prime(k: int) -> int:
    """Нахождение k-го по счёту простого числа без помощи решета Эратосфена"""
    if k == 0:
        return 2
    n = 10**6
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


if __name__ == "__main__":
    test_task(sieve)
    test_task(prime)

###############################################################################

# python3 -m timeit -n 100 -s "from les_4_task_2 import sieve" "sieve(100)"
# 100 loops, best of 5: 156 msec per loop
# python3 -m timeit -n 100 -s "from les_4_task_2 import prime" "prime(100)"
# 100 loops, best of 5: 127 usec per loop
# python3 -m timeit -n 10 -s "from les_4_task_2 import sieve" "sieve(100000)"
# 10 loops, best of 5: 178 msec per loop
# python3 -m timeit -n 10 -s "from les_4_task_2 import prime" "prime(100000)"
# 10 loops, best of 5: 1.13 sec per loop

###############################################################################

    import cProfile
    N = 100
    X = 10000
    cProfile.run("[sieve(%d) for i in range(%d)]" % (X, N))
#      100    9.003    0.090   15.905    0.159 les_4_task_2.py:28(sieve)
    cProfile.run("[prime(%d) for i in range(%d)]" % (X, N))
#  5237100    5.401    0.000    5.401    0.000 les_4_task_2.py:48(isprime)
#      100    0.793    0.008    6.194    0.062 les_4_task_2.py:60(prime)

###############################################################################
