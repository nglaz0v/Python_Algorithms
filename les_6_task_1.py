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
        items = struct.unpack('Q'*abs(info.size), ctypes.string_at(info.id_items, 8*abs(info.size)))
        for item in items:
            mem_dump(item, level+1)
    elif obj.type == id(type(set())):
        items = struct.unpack('Q'*abs(info.used)*2, ctypes.string_at(info.id_table, 8*abs(info.used)*2))
        print(items)
    elif obj.type == id(type(dict())):
        items = struct.unpack('Q'*7 + 'Q'*abs(info.used)*3, ctypes.string_at(info.id_keys, 8*7+8*abs(info.used)*3))
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
    memory_used = sum(map(sys.getsizeof, (X for _, X in fvars)))
    print(f"*** Memory used: {memory_used} bytes ***")
    print("="*20)
    return memory_used


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

# --- reverse_1 ---
# name=number id=140725472927456: value=0	class=<class 'int'>	sizeof=24
# [140725472927456]: Long(refcnt=314, type=140725472757536, size=0, digit=())
# name=result id=1778432644080: value=7085774586302733229	class=<class 'int'>	sizeof=36
# [1778432644080]: Long(refcnt=4, type=140725472757536, size=3, digit=(923835309, 156690886, 6))
# name=digit id=140725472927744: value=9	class=<class 'int'>	sizeof=28
# [140725472927744]: Long(refcnt=20, type=140725472757536, size=1, digit=(9,))
# *** Memory used: 88 bytes ***
# ====================


def reverse_2(number):
    """Инвертировать порядок цифр натурального числа (рекурсивная версия)"""
    def invert(number, mem_used=0):
        if (len(number) == 1):
            return number, 0
        else:
            head = number[1:]
            tail = number[:1]
            inv_head, mem_used = invert(head)
            result = inv_head + tail
            mem_used += func_vars(invert.__name__, locals().items())
            return result, mem_used
    print(f"--- {reverse_2.__name__} ---")
    result, mem_used = invert(str(number))
    result = int(result)
    print(f"*** Memory used: {mem_used} bytes ***")
    return result

# --- reverse_2 ---
# --- invert ---
# name=number id=1778432641968: value='70'	class=<class 'str'>	sizeof=51
# [1778432641968]: Unicode(refcnt=6, type=140725472778016, length=2, hash=-1, state1=1778432642276, state2=0, wstr=(b'7', b'0', b'\x00'))
# name=mem_used id=140725472927456: value=0	class=<class 'int'>	sizeof=24
# [140725472927456]: Long(refcnt=333, type=140725472757536, size=0, digit=())
# name=head id=1778432572208: value='0'	class=<class 'str'>	sizeof=50
# [1778432572208]: Unicode(refcnt=10, type=140725472778016, length=1, hash=8321573922247248229, state1=228, state2=0, wstr=(b'0', b'\x00'))
# name=tail id=1778432641136: value='7'	class=<class 'str'>	sizeof=50
# [1778432641136]: Unicode(refcnt=8, type=140725472778016, length=1, hash=-1, state1=228, state2=0, wstr=(b'7', b'\x00'))
# name=inv_head id=1778432572208: value='0'	class=<class 'str'>	sizeof=50
# [1778432572208]: Unicode(refcnt=10, type=140725472778016, length=1, hash=8321573922247248229, state1=228, state2=0, wstr=(b'0', b'\x00'))
# name=result id=1778432642032: value='07'	class=<class 'str'>	sizeof=51
# [1778432642032]: Unicode(refcnt=4, type=140725472778016, length=2, hash=-1, state1=515396075748, state2=0, wstr=(b'0', b'7', b'\x00'))
# name=invert id=1778432648528: value=<function reverse_2.<locals>.invert at 0x0000019E12D8A550>	class=<class 'function'>	sizeof=136
# [1778432648528]: None
# *** Memory used: 412 bytes ***
# ====================
# --- invert ---
# name=number id=1778432641904: value='070'	class=<class 'str'>	sizeof=52
# [1778432641904]: Unicode(refcnt=6, type=140725472778016, length=3, hash=-1, state1=1778432642020, state2=0, wstr=(b'0', b'7', b'0', b'\x00'))
# name=mem_used id=1778432486224: value=412	class=<class 'int'>	sizeof=28
# [1778432486224]: Long(refcnt=5, type=140725472757536, size=1, digit=(412,))
# name=head id=1778432641968: value='70'	class=<class 'str'>	sizeof=51
# [1778432641968]: Unicode(refcnt=4, type=140725472778016, length=2, hash=-1, state1=1778432642276, state2=0, wstr=(b'7', b'0', b'\x00'))
# name=tail id=1778432572208: value='0'	class=<class 'str'>	sizeof=50
# [1778432572208]: Unicode(refcnt=7, type=140725472778016, length=1, hash=8321573922247248229, state1=228, state2=0, wstr=(b'0', b'\x00'))
# name=inv_head id=1778432642032: value='07'	class=<class 'str'>	sizeof=51
# [1778432642032]: Unicode(refcnt=4, type=140725472778016, length=2, hash=-1, state1=515396075748, state2=0, wstr=(b'0', b'7', b'\x00'))
# name=result id=1778432676464: value='070'	class=<class 'str'>	sizeof=52
# [1778432676464]: Unicode(refcnt=4, type=140725472778016, length=3, hash=-1, state1=228, state2=0, wstr=(b'0', b'7', b'0', b'\x00'))
# name=invert id=1778432648528: value=<function reverse_2.<locals>.invert at 0x0000019E12D8A550>	class=<class 'function'>	sizeof=136
# [1778432648528]: None
# *** Memory used: 420 bytes ***
# ====================
# ...
# --- invert ---
# name=number id=1778432554448: value='92233720368547758070'	class=<class 'str'>	sizeof=69
# [1778432554448]: Unicode(refcnt=5, type=140725472778016, length=20, hash=-1, state1=228, state2=0, wstr=(b'9', b'2', b'2', b'3', b'3', b'7', b'2', b'0', b'3', b'6', b'8', b'5', b'4', b'7', b'7', b'5', b'8', b'0', b'7', b'0', b'\x00'))
# name=mem_used id=1778432486128: value=8096	class=<class 'int'>	sizeof=28
# [1778432486128]: Long(refcnt=5, type=140725472757536, size=1, digit=(8096,))
# name=head id=1778432577248: value='2233720368547758070'	class=<class 'str'>	sizeof=68
# [1778432577248]: Unicode(refcnt=4, type=140725472778016, length=19, hash=-1, state1=228, state2=0, wstr=(b'2', b'2', b'3', b'3', b'7', b'2', b'0', b'3', b'6', b'8', b'5', b'4', b'7', b'7', b'5', b'8', b'0', b'7', b'0', b'\x00'))
# name=tail id=1778432641008: value='9'	class=<class 'str'>	sizeof=50
# [1778432641008]: Unicode(refcnt=5, type=140725472778016, length=1, hash=-1, state1=1778432640996, state2=0, wstr=(b'9', b'\x00'))
# name=inv_head id=1778432577408: value='0708577458630273322'	class=<class 'str'>	sizeof=68
# [1778432577408]: Unicode(refcnt=4, type=140725472778016, length=19, hash=-1, state1=1778432478180, state2=0, wstr=(b'0', b'7', b'0', b'8', b'5', b'7', b'7', b'4', b'5', b'8', b'6', b'3', b'0', b'2', b'7', b'3', b'3', b'2', b'2', b'\x00'))
# name=result id=1778432577328: value='07085774586302733229'	class=<class 'str'>	sizeof=69
# [1778432577328]: Unicode(refcnt=4, type=140725472778016, length=20, hash=-1, state1=228, state2=0, wstr=(b'0', b'7', b'0', b'8', b'5', b'7', b'7', b'4', b'5', b'8', b'6', b'3', b'0', b'2', b'7', b'3', b'3', b'2', b'2', b'9', b'\x00'))
# name=invert id=1778432648528: value=<function reverse_2.<locals>.invert at 0x0000019E12D8A550>	class=<class 'function'>	sizeof=136
# [1778432648528]: None
# *** Memory used: 488 bytes ***
# ====================
# *** Memory used: 8584 bytes ***


def reverse_3(number):
    """Инвертировать порядок цифр натурального числа (версия со срезами)"""
    str_num = str(number)
    rev_str_num = str_num[::-1]
    result = int(rev_str_num)
    func_vars(reverse_3.__name__, locals().items())
    return result

# --- reverse_3 ---
# name=number id=1778432729024: value=92233720368547758070	class=<class 'int'>	sizeof=36
# [1778432729024]: Long(refcnt=9, type=140725472757536, size=3, digit=(1073741814, 1073741823, 79))
# name=str_num id=1778432554448: value='92233720368547758070'	class=<class 'str'>	sizeof=69
# [1778432554448]: Unicode(refcnt=4, type=140725472778016, length=20, hash=-1, state1=228, state2=0, wstr=(b'9', b'2', b'2', b'3', b'3', b'7', b'2', b'0', b'3', b'6', b'8', b'5', b'4', b'7', b'7', b'5', b'8', b'0', b'7', b'0', b'\x00'))
# name=rev_str_num id=1778432577328: value='07085774586302733229'	class=<class 'str'>	sizeof=69
# [1778432577328]: Unicode(refcnt=4, type=140725472778016, length=20, hash=-1, state1=228, state2=0, wstr=(b'0', b'7', b'0', b'8', b'5', b'7', b'7', b'4', b'5', b'8', b'6', b'3', b'0', b'2', b'7', b'3', b'3', b'2', b'2', b'9', b'\x00'))
# name=result id=1778432685664: value=7085774586302733229	class=<class 'int'>	sizeof=36
# [1778432685664]: Long(refcnt=4, type=140725472757536, size=3, digit=(923835309, 156690886, 6))
# *** Memory used: 210 bytes ***
# ====================


def test_reverse(n):
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
    print("-"*40)

    sX = "0123456789"  # str
    tX = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple
    lX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
    nX = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # set
    dX = {_: _ for _ in tX}  # dict

    for X in (False, True, -100, 0, 10, 10**3, 10**20, 1/2, -1j, 1-0j):
        # var_info(X)
        print(f"id={id(X)}: value={repr(X)}\tclass={type(X)}\tsizeof={sys.getsizeof(X)}\t")
        mem_dump(id(X))
        print()

    for X in (str(), tuple(), list(), set(), dict(), sX, tX, lX, nX, dX):
        # print("{}   \t{}\t{}".format(type(X), sys.getsizeof(X), struct.unpack(fmt[id(type(X))], ctypes.string_at(id(X), X.__sizeof__()))))
        # var_info(X)
        print(f"id={id(X)}: value={repr(X)}\tclass={type(X)}\tsizeof={sys.getsizeof(X)}\t")
        mem_dump(id(X))
        print()
        # total_size(X, verbose=True)
    print("="*40)


if __name__ == "__main__":
    print(f"System: {sys.platform};\tPython: {sys.version}")
    # test_mem_dump()
    test_reverse(92233720368547758070)


# System: win32;	Python: 3.8.12 (default, Oct 12 2021, 03:01:40) [MSC v.1916 64 bit (AMD64)]

# ВЫВОД:
# Для тестирования использовалось целое число, которое заведомо больше чем 2**64.
# Среди трёх функций инвертирования порядка цифр натурального числа лучшие
# результаты продемонстрировала reverse_1().
#
# reverse_1() для вычисления результата использует целочисленную арифметику и
# задействует всего три переменные типа Long (number, digit, result).
# Общее количество памяти, занятой данной функцией: ~ 88 байт
#
# reverse_2() для работы использует рекурсивную функцию invert() и за каждый её
# вызов расходуется в среднем 450 байт на строковые переменные.
# Общее количество памяти, занятой данной функцией: ~ 8584 байт
#
# reverse_3() использует механизм срезов Python3 и задействует две переменные
# типа Long (number, result) и две переменные типа Unicode (str_num, rev_str_num).
# Общее количество памяти, занятой данной функцией: ~ 210 байт
