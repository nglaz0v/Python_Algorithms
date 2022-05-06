# -*- coding: utf-8 -*-
"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter


class BinTreeNode:
    """Узел бинарного дерева"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __content(self, k=0):
        """Содержимое узла и его дочерних узлов"""
        s = ''
        if self is None:
            return s
        k += 1
        if self.left is not None:
            s += self.left.__content(k)
        s += f"{' '*k*4}'{self.data}'\n"
        if self.right is not None:
            s += self.right.__content(k)
        k -= 1
        return s

    def __str__(self):
        return self.__content()

    def __repr__(self):
        return f"'{self.data}'"


def code_table(node: BinTreeNode, tbl={}, path='') -> dict:
    """Создать таблицу кодирования"""
    if node is None:
        return
    code_table(node.left, tbl, path+'0')
    if node.left is None and node.right is None:
        tbl[node.data] = path  # int(path, base=2)
    code_table(node.right, tbl, path+'1')
    return tbl


def huffman(s: str) -> dict:
    """Кодирование по алгоритму Хаффмана"""
    freqs = dict(Counter(s))
    elems = sorted(freqs, key=freqs.get)
    leafs = [BinTreeNode(item) for item in elems]
    print(leafs)

    while len(elems) > 1:
        e_l = leafs.pop(0)
        e_r = leafs.pop(0)
        node = BinTreeNode(e_l.data + e_r.data)
        node.left = e_l
        node.right = e_r
        freqs[e_l.data + e_r.data] = freqs[e_l.data] + freqs[e_r.data]
        freqs.pop(e_l.data)
        freqs.pop(e_r.data)
        elems = sorted(freqs, key=freqs.get)
        leafs.insert(elems.index(e_l.data+e_r.data), node)
        # print(elems, end=' ')
        # print(freqs, end=' ')
        print(leafs)

    print(node)
    # print(leafs[0])
    return code_table(node)


print(__doc__)
s = input("Введите кодируемую строку: ")  # "beep boop beer!"
tbl = huffman(s)
print(tbl)
print("\nИсходная строка: ")
for c in s:
    print(f"{bin(ord(c))[2:]:0>8}", end=' ')
print()
for c in s:
    print(f"{c:<8}", end=' ')
print(f"\nДлина строки: {len(s)*8} бит")
print("\nЗакодированная строка: ")
for c in s:
    print(f"{tbl[c]}", end=' ')
print()
for c in s:
    print(f"{c}" + ' '*len(tbl[c]), end='')
print(f"\nДлина строки: {sum([len(tbl[c]) for c in s])} бит")
