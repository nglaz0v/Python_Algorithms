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

Object = namedtuple("Object", ("refcnt", "type"))
VarObject = namedtuple("VarObject", Object._fields + ("size",))
Long = namedtuple("Long", VarObject._fields + ("digit",), defaults=[0])
Float = namedtuple("Float", Object._fields + ("fval",))
Complex = namedtuple("Complex", Object._fields + ("real", "imag"))
Bool = namedtuple("Bool", Long._fields, defaults=[0])
Unicode = namedtuple("Unicode", Object._fields + ("length", "hash", "state1", "state2", "wstr"))
Tuple = namedtuple("Tuple", VarObject._fields + ("items",))
List = namedtuple("List", VarObject._fields + ("id_items", "allocated"))
Set = namedtuple("Set", Object._fields + ("fill", "used", "mask", "id_table", "hash", "finger", "smalltable"))
Dict = namedtuple("Dict", Object._fields + ("used", "version_tag", "id_keys", "id_values"))


def mem_dump(addr, level=0):
    """Информация о данных в памяти по заданному адресу"""
    fmt_py_obj = 'nP'  # ob_refcnt + ob_type
    sz_py_obj = 8 + 8
    fmt_py_obj_var = fmt_py_obj + 'n'  # ... + ob_size
    sz_py_obj_var = sz_py_obj + 8

    head = struct.unpack(fmt_py_obj, ctypes.string_at(addr, sz_py_obj))
    obj = Object._make(head)

    var_head = struct.unpack(fmt_py_obj_var, ctypes.string_at(addr, sz_py_obj_var))
    var_obj = VarObject._make(var_head)

    info = None
    if (obj.type == id(type(int()))) or (obj.type == id(type(bool()))):
        fmt = fmt_py_obj_var + 'i'*abs(var_obj.size)  # ... + ob_digit
        size = sz_py_obj_var + 4*abs(var_obj.size)
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        if (obj.type == id(type(bool()))):
            assert abs(var_obj.size) < 2
            info = Bool(*dump)
        else:
            k = len(Long._fields) - 1
            info = Long(*(*(dump[:k]), dump[k:]))
    elif obj.type == id(type(float())):
        fmt = fmt_py_obj + 'd'  # ... + ob_fval
        size = sz_py_obj + 8
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        info = Float(*dump)
    elif obj.type == id(type(complex())):
        fmt = fmt_py_obj + 'dd'  # ... + real + imag
        size = sz_py_obj + 8*2
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        info = Complex(*dump)
    elif obj.type == id(type(str())):
        len_x = abs(var_obj.size)
        fmt = fmt_py_obj_var + 'nQQ' + 'c'*(len_x+1)  # ... + hash + state1 + state2 + wstr
        size = sz_py_obj_var + 8*3 + abs(len_x+1)
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        k = len(Unicode._fields) - 1
        info = Unicode(*(*(dump[:k]), dump[k:]))
    elif obj.type == id(type(tuple())):
        fmt = fmt_py_obj_var + 'P'*abs(var_obj.size)  # ... + ob_item
        size = sz_py_obj_var + 8*abs(var_obj.size)
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        k = len(Tuple._fields) - 1
        info = Tuple(*(*(dump[:k]), dump[k:]))
    elif obj.type == id(type(list())):
        fmt = fmt_py_obj_var + 'Pn'  # ... + ob_item + allocated
        size = sz_py_obj_var + 8*2
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        info = List(*dump)
    elif obj.type == id(type(set())):
        fmt = fmt_py_obj + 'nnnPnn' + 'Pn'*8 + 'P'  # ... + fill + used + mask + table + hash + finger + smalltable + weakreflist
        size = sz_py_obj + 8*6 + 8*2*8 + 8
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        k = len(Set._fields) - 1
        info = Set(*(*(dump[:k]), dump[k:]))
    elif obj.type == id(type(dict())):
        fmt = fmt_py_obj + 'nLPP'  # ... + ma_used + ma_version_tag + ma_keys + ma_values
        size = sz_py_obj+8*4
        dump = struct.unpack(fmt, ctypes.string_at(addr, size))
        info = Dict(*dump)
    print('\t' * level + f"[{addr}]: {info}")
    if obj.type == id(type(tuple())):
        for item in info.items:
            mem_dump(item, level+1)
    elif obj.type == id(type(list())):
        items = struct.unpack('L'*abs(info.size), ctypes.string_at(info.id_items, 8*abs(var_obj.size)))
        for item in items:
            mem_dump(item, level+1)
    elif obj.type == id(type(set())):
        items = struct.unpack('L'*abs(info.used)*2, ctypes.string_at(info.id_table, 8*abs(var_obj.size)*2))
        print(items)
    elif obj.type == id(type(dict())):
        items = struct.unpack('L'*7 + 'L'*abs(info.used)*3, ctypes.string_at(info.id_keys, 8*7+8*abs(var_obj.size)*3))
        print(items)
    return info


def var_info(x, level=0):
    """Информация о переменной"""
    print('\t' * level + f"id={id(x)}: sizeof={x.__sizeof__()},\t"
                         f"refcount={sys.getrefcount(x)},\ttype={type(x)},\t"
                         f"value={repr(x)}")
    # mem_dump(id(x), x.__sizeof__())
    if hasattr(x, "__iter__"):
        if isinstance(x, dict):
            for k in x:
                var_info(k, level+1)
                var_info(x[k], level+1)
        elif not isinstance(x, str):
            for xx in x:
                var_info(xx, level+1)


def total_size(obj, verbose=False):
    """Приблизительный объём памяти объекта и всего его содержимого"""
    seen = set()  # чтобы отслеживать, какие объекты уже были учтены
    default_size = sys.getsizeof(0)  # оценить размер объекта без __sizeof__

    def sizeof(obj):
        if id(obj) in seen:  # не учитывать один и тот же объект дважды
            return 0
        seen.add(id(obj))
        s = sys.getsizeof(obj, default_size)
        if verbose:
            print(f"{s} {type(obj)} {repr(obj)}")
        if hasattr(obj, "__iter__"):
            if isinstance(obj, dict):
                s += sum(map(sizeof, iter(obj.keys())))
                s += sum(map(sizeof, iter(obj.values())))
            elif not isinstance(obj, str):
                s += sum(map(sizeof, iter(obj)))
        return s

    return sizeof(obj)


def func_vars(fname, fvars):
    print(f"--- {fname} ---")
    for name, X in fvars:
        print(f"name={name} id={id(X)}: value={repr(X)}\tclass={type(X)}\tsizeof={sys.getsizeof(X)}\t")
        mem_dump(id(X))
    print("="*20)


def reverse_1(number):
    """Инвертировать порядок цифр натурального числа (числовая версия)"""
    result = 0
    while (number > 0):
        digit = number % 10
        result *= 10
        result += digit
        number //= 10
    func_vars(reverse_1.__name__, locals().items())
    return result


def reverse_2(number):
    """Инвертировать порядок цифр натурального числа (рекурсивная версия)"""
    def invert(number):
        if (len(number) == 1):
            return number
        else:
            head = number[1:]
            tail = number[:1]
            inv_head = invert(head)
            result = inv_head + tail
            func_vars(reverse_2.__name__, locals().items())
            return result
    return int(invert(str(number)))


def reverse_3(number):
    """Инвертировать порядок цифр натурального числа (версия со срезами)"""
    str_num = str(number)
    rev_str_num = str_num[::-1]
    result = int(rev_str_num)
    func_vars(reverse_3.__name__, locals().items())
    return result


def test_task(n):
    """Проверка: сравнение значений функций reverse() между собой"""
    a = reverse_1(n)
    b = reverse_2(n)
    c = reverse_3(n)
    print("%d : %d = %d = %d" % (n, a, b, c))
    assert a == b == c


def test_mem_dump():
    """Проверка: тестирование функций работы с памятью"""
    # d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    # print(total_size(d, verbose=True))

    sX = "0123456789"  # str
    tX = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple
    lX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
    nX = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # set
    dX = {_: _ for _ in tX}  # dict

    for X in (False, True, -100, 0, 10, 10**3, 10**20, 1/2, -1j, 1-0j):
        # var_info(X)
        print(f"id={id(X)}: value={repr(X)}\tclass={type(X)}\tsizeof={sys.getsizeof(X)}\t", end='')
        mem_dump(id(X))

    for X in (str(), tuple(), list(), set(), dict(), sX, tX, lX, nX, dX):
        # print("{}   \t{}\t{}".format(type(X), sys.getsizeof(X), struct.unpack(fmt[id(type(X))], ctypes.string_at(id(X), X.__sizeof__()))))
        var_info(X)
        print(f"id={id(X)}: value={repr(X)}\tclass={type(X)}\tsizeof={sys.getsizeof(X)}\t")
        mem_dump(id(X))
        # total_size(X, verbose=True)


if __name__ == "__main__":
    print(f"System: {sys.platform};\tPython: {sys.version}")
    # test_mem_dump()
    test_task(92233720368547758070)


# TODO: ВЫВОД
