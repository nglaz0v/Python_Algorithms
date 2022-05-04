# -*- coding: utf-8 -*-
"""
Определение количества различных подстрок с использованием хеш-функции. Пусть
на вход функции дана строка. Требуется вернуть количество различных подстрок в
этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой
  другой из модуля hashlib) задача считается не решённой.
"""

import hashlib


def count_substrs(s: str) -> int:
    """
    Определить количество различных подстрок в заданной строке
    """
    s = s.lower()
    n = len(s)
    assert n > 0, "Строка не может быть пустой"
    hashes = set()
    for k in range(1, n):
        for i in range(n - k + 1):
            substr = s[i:i+k]
            print(f"{k} {i}: {substr}")
            hashsub = hashlib.sha1(substr.encode("utf-8")).hexdigest()
            hashes.add(hashsub)
    return len(hashes)


print(__doc__)
s = input("Введите строку: ")
print(f"Количество различных подстрок в данной строке: {count_substrs(s)}")
