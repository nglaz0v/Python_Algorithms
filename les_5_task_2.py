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

from collections import Counter, deque, defaultdict, OrderedDict, namedtuple


def hexsum(a: list, b: list) -> list:
    """Сложение двух шестнадцатеричных чисел"""
    ValueCarry = namedtuple("ValueCarry", "value carry")
    addition_table = {
            ('0', '0'): ValueCarry('0', '0'),
            ('0', '1'): ValueCarry('1', '0'),
            ('0', '2'): ValueCarry('2', '0'),
            ('0', '3'): ValueCarry('3', '0'),
            ('0', '4'): ValueCarry('4', '0'),
            ('0', '5'): ValueCarry('5', '0'),
            ('0', '6'): ValueCarry('6', '0'),
            ('0', '7'): ValueCarry('7', '0'),
            ('0', '8'): ValueCarry('8', '0'),
            ('0', '9'): ValueCarry('9', '0'),
            ('0', 'A'): ValueCarry('A', '0'),
            ('0', 'B'): ValueCarry('B', '0'),
            ('0', 'C'): ValueCarry('C', '0'),
            ('0', 'D'): ValueCarry('D', '0'),
            ('0', 'E'): ValueCarry('E', '0'),
            ('0', 'F'): ValueCarry('F', '0'),
            ('1', '0'): ValueCarry('1', '0'),
            ('1', '1'): ValueCarry('2', '0'),
            ('1', '2'): ValueCarry('3', '0'),
            ('1', '3'): ValueCarry('4', '0'),
            ('1', '4'): ValueCarry('5', '0'),
            ('1', '5'): ValueCarry('6', '0'),
            ('1', '6'): ValueCarry('7', '0'),
            ('1', '7'): ValueCarry('8', '0'),
            ('1', '8'): ValueCarry('9', '0'),
            ('1', '9'): ValueCarry('A', '0'),
            ('1', 'A'): ValueCarry('B', '0'),
            ('1', 'B'): ValueCarry('C', '0'),
            ('1', 'C'): ValueCarry('D', '0'),
            ('1', 'D'): ValueCarry('E', '0'),
            ('1', 'E'): ValueCarry('F', '0'),
            ('1', 'F'): ValueCarry('0', '1'),
            ('2', '0'): ValueCarry('2', '0'),
            ('2', '1'): ValueCarry('3', '0'),
            ('2', '2'): ValueCarry('4', '0'),
            ('2', '3'): ValueCarry('5', '0'),
            ('2', '4'): ValueCarry('6', '0'),
            ('2', '5'): ValueCarry('7', '0'),
            ('2', '6'): ValueCarry('8', '0'),
            ('2', '7'): ValueCarry('9', '0'),
            ('2', '8'): ValueCarry('A', '0'),
            ('2', '9'): ValueCarry('B', '0'),
            ('2', 'A'): ValueCarry('C', '0'),
            ('2', 'B'): ValueCarry('D', '0'),
            ('2', 'C'): ValueCarry('E', '0'),
            ('2', 'D'): ValueCarry('F', '0'),
            ('2', 'E'): ValueCarry('0', '1'),
            ('2', 'F'): ValueCarry('1', '1'),
            ('3', '0'): ValueCarry('3', '0'),
            ('3', '1'): ValueCarry('4', '0'),
            ('3', '2'): ValueCarry('5', '0'),
            ('3', '3'): ValueCarry('6', '0'),
            ('3', '4'): ValueCarry('7', '0'),
            ('3', '5'): ValueCarry('8', '0'),
            ('3', '6'): ValueCarry('9', '0'),
            ('3', '7'): ValueCarry('A', '0'),
            ('3', '8'): ValueCarry('B', '0'),
            ('3', '9'): ValueCarry('C', '0'),
            ('3', 'A'): ValueCarry('D', '0'),
            ('3', 'B'): ValueCarry('E', '0'),
            ('3', 'C'): ValueCarry('F', '0'),
            ('3', 'D'): ValueCarry('0', '1'),
            ('3', 'E'): ValueCarry('1', '1'),
            ('3', 'F'): ValueCarry('2', '1'),
            ('4', '0'): ValueCarry('4', '0'),
            ('4', '1'): ValueCarry('5', '0'),
            ('4', '2'): ValueCarry('6', '0'),
            ('4', '3'): ValueCarry('7', '0'),
            ('4', '4'): ValueCarry('8', '0'),
            ('4', '5'): ValueCarry('9', '0'),
            ('4', '6'): ValueCarry('A', '0'),
            ('4', '7'): ValueCarry('B', '0'),
            ('4', '8'): ValueCarry('C', '0'),
            ('4', '9'): ValueCarry('D', '0'),
            ('4', 'A'): ValueCarry('E', '0'),
            ('4', 'B'): ValueCarry('F', '0'),
            ('4', 'C'): ValueCarry('0', '1'),
            ('4', 'D'): ValueCarry('1', '1'),
            ('4', 'E'): ValueCarry('2', '1'),
            ('4', 'F'): ValueCarry('3', '1'),
            ('5', '0'): ValueCarry('5', '0'),
            ('5', '1'): ValueCarry('6', '0'),
            ('5', '2'): ValueCarry('7', '0'),
            ('5', '3'): ValueCarry('8', '0'),
            ('5', '4'): ValueCarry('9', '0'),
            ('5', '5'): ValueCarry('A', '0'),
            ('5', '6'): ValueCarry('B', '0'),
            ('5', '7'): ValueCarry('C', '0'),
            ('5', '8'): ValueCarry('D', '0'),
            ('5', '9'): ValueCarry('E', '0'),
            ('5', 'A'): ValueCarry('F', '0'),
            ('5', 'B'): ValueCarry('0', '1'),
            ('5', 'C'): ValueCarry('1', '1'),
            ('5', 'D'): ValueCarry('2', '1'),
            ('5', 'E'): ValueCarry('3', '1'),
            ('5', 'F'): ValueCarry('4', '1'),
            ('6', '0'): ValueCarry('6', '0'),
            ('6', '1'): ValueCarry('7', '0'),
            ('6', '2'): ValueCarry('8', '0'),
            ('6', '3'): ValueCarry('9', '0'),
            ('6', '4'): ValueCarry('A', '0'),
            ('6', '5'): ValueCarry('B', '0'),
            ('6', '6'): ValueCarry('C', '0'),
            ('6', '7'): ValueCarry('D', '0'),
            ('6', '8'): ValueCarry('E', '0'),
            ('6', '9'): ValueCarry('F', '0'),
            ('6', 'A'): ValueCarry('0', '1'),
            ('6', 'B'): ValueCarry('1', '1'),
            ('6', 'C'): ValueCarry('2', '1'),
            ('6', 'D'): ValueCarry('3', '1'),
            ('6', 'E'): ValueCarry('4', '1'),
            ('6', 'F'): ValueCarry('5', '1'),
            ('7', '0'): ValueCarry('7', '0'),
            ('7', '1'): ValueCarry('8', '0'),
            ('7', '2'): ValueCarry('9', '0'),
            ('7', '3'): ValueCarry('A', '0'),
            ('7', '4'): ValueCarry('B', '0'),
            ('7', '5'): ValueCarry('C', '0'),
            ('7', '6'): ValueCarry('D', '0'),
            ('7', '7'): ValueCarry('E', '0'),
            ('7', '8'): ValueCarry('F', '0'),
            ('7', '9'): ValueCarry('0', '1'),
            ('7', 'A'): ValueCarry('1', '1'),
            ('7', 'B'): ValueCarry('2', '1'),
            ('7', 'C'): ValueCarry('3', '1'),
            ('7', 'D'): ValueCarry('4', '1'),
            ('7', 'E'): ValueCarry('5', '1'),
            ('7', 'F'): ValueCarry('6', '1'),
            ('8', '0'): ValueCarry('8', '0'),
            ('8', '1'): ValueCarry('9', '0'),
            ('8', '2'): ValueCarry('A', '0'),
            ('8', '3'): ValueCarry('B', '0'),
            ('8', '4'): ValueCarry('C', '0'),
            ('8', '5'): ValueCarry('D', '0'),
            ('8', '6'): ValueCarry('E', '0'),
            ('8', '7'): ValueCarry('F', '0'),
            ('8', '8'): ValueCarry('0', '1'),
            ('8', '9'): ValueCarry('1', '1'),
            ('8', 'A'): ValueCarry('2', '1'),
            ('8', 'B'): ValueCarry('3', '1'),
            ('8', 'C'): ValueCarry('4', '1'),
            ('8', 'D'): ValueCarry('5', '1'),
            ('8', 'E'): ValueCarry('6', '1'),
            ('8', 'F'): ValueCarry('7', '1'),
            ('9', '0'): ValueCarry('9', '0'),
            ('9', '1'): ValueCarry('A', '0'),
            ('9', '2'): ValueCarry('B', '0'),
            ('9', '3'): ValueCarry('C', '0'),
            ('9', '4'): ValueCarry('D', '0'),
            ('9', '5'): ValueCarry('E', '0'),
            ('9', '6'): ValueCarry('F', '0'),
            ('9', '7'): ValueCarry('0', '1'),
            ('9', '8'): ValueCarry('1', '1'),
            ('9', '9'): ValueCarry('2', '1'),
            ('9', 'A'): ValueCarry('3', '1'),
            ('9', 'B'): ValueCarry('4', '1'),
            ('9', 'C'): ValueCarry('5', '1'),
            ('9', 'D'): ValueCarry('6', '1'),
            ('9', 'E'): ValueCarry('7', '1'),
            ('9', 'F'): ValueCarry('8', '1'),
            ('A', '0'): ValueCarry('A', '0'),
            ('A', '1'): ValueCarry('B', '0'),
            ('A', '2'): ValueCarry('C', '0'),
            ('A', '3'): ValueCarry('D', '0'),
            ('A', '4'): ValueCarry('E', '0'),
            ('A', '5'): ValueCarry('F', '0'),
            ('A', '6'): ValueCarry('0', '1'),
            ('A', '7'): ValueCarry('1', '1'),
            ('A', '8'): ValueCarry('2', '1'),
            ('A', '9'): ValueCarry('3', '1'),
            ('A', 'A'): ValueCarry('4', '1'),
            ('A', 'B'): ValueCarry('5', '1'),
            ('A', 'C'): ValueCarry('6', '1'),
            ('A', 'D'): ValueCarry('7', '1'),
            ('A', 'E'): ValueCarry('8', '1'),
            ('A', 'F'): ValueCarry('9', '1'),
            ('B', '0'): ValueCarry('B', '0'),
            ('B', '1'): ValueCarry('C', '0'),
            ('B', '2'): ValueCarry('D', '0'),
            ('B', '3'): ValueCarry('E', '0'),
            ('B', '4'): ValueCarry('F', '0'),
            ('B', '5'): ValueCarry('0', '1'),
            ('B', '6'): ValueCarry('1', '1'),
            ('B', '7'): ValueCarry('2', '1'),
            ('B', '8'): ValueCarry('3', '1'),
            ('B', '9'): ValueCarry('4', '1'),
            ('B', 'A'): ValueCarry('5', '1'),
            ('B', 'B'): ValueCarry('6', '1'),
            ('B', 'C'): ValueCarry('7', '1'),
            ('B', 'D'): ValueCarry('8', '1'),
            ('B', 'E'): ValueCarry('9', '1'),
            ('B', 'F'): ValueCarry('A', '1'),
            ('C', '0'): ValueCarry('C', '0'),
            ('C', '1'): ValueCarry('D', '0'),
            ('C', '2'): ValueCarry('E', '0'),
            ('C', '3'): ValueCarry('F', '0'),
            ('C', '4'): ValueCarry('0', '1'),
            ('C', '5'): ValueCarry('1', '1'),
            ('C', '6'): ValueCarry('2', '1'),
            ('C', '7'): ValueCarry('3', '1'),
            ('C', '8'): ValueCarry('4', '1'),
            ('C', '9'): ValueCarry('5', '1'),
            ('C', 'A'): ValueCarry('6', '1'),
            ('C', 'B'): ValueCarry('7', '1'),
            ('C', 'C'): ValueCarry('8', '1'),
            ('C', 'D'): ValueCarry('9', '1'),
            ('C', 'E'): ValueCarry('A', '1'),
            ('C', 'F'): ValueCarry('B', '1'),
            ('D', '0'): ValueCarry('D', '0'),
            ('D', '1'): ValueCarry('E', '0'),
            ('D', '2'): ValueCarry('F', '0'),
            ('D', '3'): ValueCarry('0', '1'),
            ('D', '4'): ValueCarry('1', '1'),
            ('D', '5'): ValueCarry('2', '1'),
            ('D', '6'): ValueCarry('3', '1'),
            ('D', '7'): ValueCarry('4', '1'),
            ('D', '8'): ValueCarry('5', '1'),
            ('D', '9'): ValueCarry('6', '1'),
            ('D', 'A'): ValueCarry('7', '1'),
            ('D', 'B'): ValueCarry('8', '1'),
            ('D', 'C'): ValueCarry('9', '1'),
            ('D', 'D'): ValueCarry('A', '1'),
            ('D', 'E'): ValueCarry('B', '1'),
            ('D', 'F'): ValueCarry('C', '1'),
            ('E', '0'): ValueCarry('E', '0'),
            ('E', '1'): ValueCarry('F', '0'),
            ('E', '2'): ValueCarry('0', '1'),
            ('E', '3'): ValueCarry('1', '1'),
            ('E', '4'): ValueCarry('2', '1'),
            ('E', '5'): ValueCarry('3', '1'),
            ('E', '6'): ValueCarry('4', '1'),
            ('E', '7'): ValueCarry('5', '1'),
            ('E', '8'): ValueCarry('6', '1'),
            ('E', '9'): ValueCarry('7', '1'),
            ('E', 'A'): ValueCarry('8', '1'),
            ('E', 'B'): ValueCarry('9', '1'),
            ('E', 'C'): ValueCarry('A', '1'),
            ('E', 'D'): ValueCarry('B', '1'),
            ('E', 'E'): ValueCarry('C', '1'),
            ('E', 'F'): ValueCarry('D', '1'),
            ('F', '0'): ValueCarry('F', '0'),
            ('F', '1'): ValueCarry('0', '1'),
            ('F', '2'): ValueCarry('1', '1'),
            ('F', '3'): ValueCarry('2', '1'),
            ('F', '4'): ValueCarry('3', '1'),
            ('F', '5'): ValueCarry('4', '1'),
            ('F', '6'): ValueCarry('5', '1'),
            ('F', '7'): ValueCarry('6', '1'),
            ('F', '8'): ValueCarry('7', '1'),
            ('F', '9'): ValueCarry('8', '1'),
            ('F', 'A'): ValueCarry('9', '1'),
            ('F', 'B'): ValueCarry('A', '1'),
            ('F', 'C'): ValueCarry('B', '1'),
            ('F', 'D'): ValueCarry('C', '1'),
            ('F', 'E'): ValueCarry('D', '1'),
            ('F', 'F'): ValueCarry('E', '1')
    }
    c = []
    a = a[::-1]
    b = b[::-1]
    alen = len(a)
    blen = len(b)
    if (alen < blen):
        a += ['0' for _ in range(blen-alen)]
    elif (blen < alen):
        b += ['0' for _ in range(alen-blen)]
    # print(a)
    # print(b)
    carry = '0'
    for i in range(min(len(a), len(b))):
        add = addition_table[(a[i], b[i])]
        digit = addition_table[(add.value, carry)]
        # print(f"{add=} {digit=} {carry=}")
        c.append(digit.value)
        carry = '1' if (add.carry == '1') or (digit.carry == '1') else '0'
    if carry == '1':
        c.append('1')
    return c[::-1]


def hexmul(a: list, b: list) -> list:
    """Умножение двух шестнадцатеричных чисел"""
    return ['1']


print(__doc__)
a = list(input("A: ").upper())
b = list(input("B: ").upper())
s = hexsum(a, b)
#m = hexmul(a, b)
print(f"{''.join(a)} + {''.join(b)} = {''.join(s)}")
#print(f"{''.join(a)} * {''.join(b)} = {''.join(m)}")

#for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
#    for j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
#        k = int(i, 16) + int(j, 16)
#        print(f"('{i}', '{j}'): ValueCarry('{hex(k & 15)[2:].upper()}', '{k >> 4}'),")
