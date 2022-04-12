# -*- coding: utf-8 -*-
"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования
систем счисления, задача решается в несколько строк. Для прокачки
алгоритмического мышления такой вариант не подходит. Поэтому использование
встроенных функций для перевода из одной системы счисления в другую в данной
задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import deque


hex2int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
           }
int2hex = "0123456789ABCDEF"


def hexsum(x: list, y: list) -> list:
    """Сложение двух шестнадцатеричных чисел"""
    result = deque()
    a = deque(x)
    b = deque(y)
    alen, blen = len(a), len(b)
    # выровнять a и b по длине (дополнить слева нулями)
    a.extendleft(['0'] * (blen-alen))
    b.extendleft(['0'] * (alen-blen))
    assert(len(a) == len(b))
    carry = 0  # перенос в следующий разряд
    for i in range(len(a)):
        value = hex2int[a.pop()] + hex2int[b.pop()] + carry
        digit = int2hex[value & 0xF]  # получить очередную цифру результата
        result.appendleft(digit)
        carry = value >> 4
        assert(carry < 2)
    if carry == 1:
        result.appendleft('1')
    return list(result)


def hexmul(x: list, y: list) -> list:
    """Умножение двух шестнадцатеричных чисел"""
    result = ['0']
    b = deque(y)
    for j in range(len(b)):
        item = deque()  # промежуточный результат
        a = deque(x)
        extra = 0  # перенос в следующий разряд
        for i in range(len(a)):
            value = hex2int[a[-1]] * hex2int[b[-1]] + extra
            digit = int2hex[value & 0xF]  # получить очередную цифру результата
            item.appendleft(digit)
            extra = value >> 4
            assert(extra < 16)
            a.pop()
        if extra != 0:
            item.appendleft(int2hex[extra])
        item.extend(['0'] * j)  # дополнить нулями справа
        # print(f"{item=}")
        b.pop()
        result = hexsum(result, list(item))  # прибавить промежуточный результат
    return result


def calculate(A: str, B: str):
    """Сложение/умножение двух шестнадцатеричных чисел"""
    a = list(A.upper())
    b = list(B.upper())
    s = hexsum(a, b)
    m = hexmul(a, b)
    print(f"{''.join(a)} + {''.join(b)} = {''.join(s)}")
    print(f"{''.join(a)} * {''.join(b)} = {''.join(m)}")
    assert(int(A, 16) + int(B, 16) == int(''.join(s), 16))
    assert(int(A, 16) * int(B, 16) == int(''.join(m), 16))


print(__doc__)
# A = input("A: ")
# B = input("B: ")
import random
A = hex(random.randint(0, 1000))[2:]
B = hex(random.randint(0, 1000))[2:]
calculate(A, B)
