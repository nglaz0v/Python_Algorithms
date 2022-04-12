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


hex2bin = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
           }
bin2hex = "0123456789ABCDEF"


def hexsum(x: list, y: list) -> list:
    """Сложение двух шестнадцатеричных чисел"""
    result = deque()
    a = deque(x[::-1])
    b = deque(y[::-1])
    alen = len(a)
    blen = len(b)
    a.extend(['0'] * (blen-alen))
    b.extend(['0'] * (alen-blen))
    assert(len(a) == len(b))
    carry = 0
    for i in range(len(a)):
        value = hex2bin[a[i]] + hex2bin[b[i]] + carry
        digit = bin2hex[value & 0xF]
        result.appendleft(digit)
        carry = value >> 4
        assert(carry < 2)
    if carry == 1:
        result.appendleft('1')
    return list(result)


def hexmul(x: list, y: list) -> list:
    """Умножение двух шестнадцатеричных чисел"""
    result = ['0']
    a = deque(x[::-1])
    b = deque(y[::-1])
    if (len(a) < len(b)):
        a, b = b, a
    for j in range(len(b)):
        item = deque()
        extra = 0
        for i in range(len(a)):
            value = hex2bin[a[i]] * hex2bin[b[j]] + extra
            digit = bin2hex[value & 0xF]
            item.appendleft(digit)
            extra = value >> 4
            assert(extra < 16)
        if extra != 0:
            item.appendleft(bin2hex[extra])
        item.extend(['0'] * j)
        # print(f"{item=}")
        result = hexsum(result, list(item))
    return result


def calculate(A: str, B: str):
    a = list(A.upper())
    b = list(B.upper())
    s = hexsum(a, b)
    m = hexmul(a, b)
    print(f"{''.join(a)} + {''.join(b)} = {''.join(s)}")
    print(f"{''.join(a)} * {''.join(b)} = {''.join(m)}")


print(__doc__)
# calculate(input("A: "), input("B: "))
for (A, B) in [("A2", "C4F"), ("ff", "1"), ("ff", "2")]:
    calculate(A, B)
