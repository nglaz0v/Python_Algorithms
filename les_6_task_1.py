# -*- coding: utf-8 -*-
"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трёх уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением
будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
c. проанализировать 3 варианта и выбрать оптимальный;
d. результаты анализа (количество занятой памяти в вашей среде разработки)
   вставить в виде комментариев в файл с кодом. Не забудьте указать версию и
   разрядность вашей ОС и интерпретатора Python;
e. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
после каждой переменной, а проявили творчество, фантазию и создали
универсальный код для замера памяти.
"""

import sys
import ctypes
import struct
from collections import namedtuple
# from itertools import chain


def mem_dump(x):
    Object = namedtuple("Object", ("refcnt", "type"))
    VarObject = namedtuple("VarObject", Object._fields + ("size",))
    Long = namedtuple("Long", VarObject._fields + ("digit",), defaults=[0])
    Float = namedtuple("Float", Object._fields + ("fval",))
    Complex = namedtuple("Complex", Object._fields + ("real", "imag"))
    Bool = namedtuple("Bool", Long._fields)
    Bytes = namedtuple("Bytes", VarObject._fields + ("shash", "undef1", "undef2", "chars"))
    Tuple = namedtuple("Tuple", VarObject._fields + ("items",))
    List = namedtuple("List", VarObject._fields + ("id_items", "allocated"))
    Set = namedtuple("Set", Object._fields + ("fill", "used", "mask", "id_table", "hash", "finger", "smalltable"))
    Dict = namedtuple("Dict", Object._fields + ("used", "version_tag", "id_keys", "id_values"))

    fmt_py_obj = 'nP'  # ob_refcnt + ob_type
    sz_py_obj = 8 + 8
    fmt_py_obj_var = fmt_py_obj + 'n'  # ... + ob_size
    sz_py_obj_var = sz_py_obj + 8

    addr = id(x)
    size = x.__sizeof__()
    if isinstance(x, int):
        header = struct.unpack(fmt_py_obj_var, ctypes.string_at(addr, sz_py_obj_var))
        var_obj = VarObject._make(header)
        fmt = fmt_py_obj_var + 'i'*var_obj.size  # ... + ob_digit
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        if isinstance(x, bool):
            assert var_obj.size < 2
            print(Bool(*dump))
        else:
            print(Long(*dump))
    elif isinstance(x, float):
        fmt = fmt_py_obj + 'd'  # ... + ob_fval
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(Float._make(dump))
    elif isinstance(x, complex):
        fmt = fmt_py_obj + 'dd'  # ... + real + imag
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(Complex._make(dump))
    elif isinstance(x, str):
        fmt = fmt_py_obj_var + 'nQQ' + 'c'*(len(x)+1)  # ... + ob_shash + QW + QW + ...
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(dump)
    elif isinstance(x, tuple):
        fmt = fmt_py_obj_var + 'P'*len(x)  # ... + ob_item + ...
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(dump)
    elif isinstance(x, list):
        fmt = fmt_py_obj_var + 'Pn' + 'P'*len(x)  # ... + ob_item + allocated + ...
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(dump)
    elif isinstance(x, set):
        fmt = fmt_py_obj + 'nnnPnn' + 'Pn'*8 + 'P' + 'P'*64  # ... + fill + used + mask + table + hash + finger + smalltable + weakreflist + ...
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(dump)
    elif isinstance(x, dict):
        fmt = fmt_py_obj + 'n' + 'PPP'*len(x) + 'P'*len(x)  # ... + ma_used + ...
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        print(dump)


def var_info(x, level=0):
    """Информация о переменной"""
    print('\t' * level, f"id={id(x)}: refcount={sys.getrefcount(x)},\t"
                        f"type={type(x)},\tsize={x.__sizeof__()},\t"
                        f"value={repr(x)}")
    mem_dump(x)
    if hasattr(x, "__iter__"):
        if isinstance(x, dict):
            for k in x:
                var_info(k, level+1)
                var_info(x[k], level+1)
        elif not isinstance(x, str):
            for xx in x:
                var_info(xx, level+1)


#def total_size(o, verbose=False):
#    """Returns the approximate memory footprint an object and all of its contents."""
#    all_handlers = {tuple: iter,
#                    frozenset: iter,
#                    list: iter,
#                    set: iter,
#                    dict: lambda d: chain.from_iterable(d.items())
#                    }
#    seen = set()  # track which object id's have already been seen
#    default_size = sys.getsizeof(0)  # estimate sizeof object without __sizeof__

#    def sizeof(o):
#        if id(o) in seen:  # do not double count the same object
#            return 0
#        seen.add(id(o))
#        s = sys.getsizeof(o, default_size)
#        if verbose:
#            print(s, type(o), repr(o))
#        for typ, handler in all_handlers.items():
#            if isinstance(o, typ):
#                s += sum(map(sizeof, handler(o)))
#                break
#        return s

#    return sizeof(o)


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


if __name__ == "__main__":
    test_task(92233720368547758070)

    # d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    # print(total_size(d, verbose=True))

    # неизменяемые типы
    bX = True  # bool
    iX = 5  # int
    fX = 125.54  # float
    cX = 1-1j  # complex
    sX = "Hello, world!"  # str
    tX = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple
    # fsX = frozenset(tX)  # frozenset
    # изменяемые типы
    lX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
    nX = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # set
    dX = {_: _ for _ in lX}  # dict

    fmt_py_obj = 'nP'  # ob_refcnt + ob_type
    fmt_py_obj_var = fmt_py_obj + 'n'  # ... + ob_size
    fmt = {
        id(type(iX)): fmt_py_obj_var + 'i',  # ... + ob_digit
        id(type(fX)): fmt_py_obj + 'd',  # ... + ob_fval
        id(type(cX)): fmt_py_obj + 'dd',  # ... + real + imag
        id(type(sX)): fmt_py_obj_var + 'nQQ' + 'c'*(len(sX)+1),  # ... + ob_shash + QW + QW + ...
        id(type(tX)): fmt_py_obj_var + 'P'*len(tX),  # ... + ob_item + ...
        id(type(lX)): fmt_py_obj_var + 'Pn' + 'P'*len(lX),  # ... + ob_item + allocated + ...
        id(type(nX)): fmt_py_obj + 'nnnPnn' + 'Pn'*8 + 'P' + 'P'*64,  # ... + fill + used + mask + table + hash + finger + smalltable + weakreflist + ...
        id(type(dX)): fmt_py_obj + 'n' + 'PPP'*len(dX) + 'P'*len(dX),  # ... + ma_used + ...
        id(type(bX)): fmt_py_obj_var + 'i'  # ... + ob_digit
        }
    # print(fmt)

    for X in (bX, iX, fX, cX, sX, tX, lX, nX, dX):
        print("{}   \t{}\t{}".format(type(X), sys.getsizeof(X), struct.unpack(fmt[id(type(X))], ctypes.string_at(id(X), X.__sizeof__()))))
        var_info(X)
        # total_size(X, verbose=True)


# TODO: ВЫВОД
