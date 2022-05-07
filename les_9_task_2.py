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
        k += 1  # увеличить отступ
        if self.left is not None:
            s += self.left.__content(k)  # содержимое левого поддерева
        s += f"{' '*k*4}'{self.data}'\n"  # содержимое самого узла
        if self.right is not None:
            s += self.right.__content(k)  # содержимое правого поддерева
        k -= 1  # уменьшить отступ
        return s

    def __str__(self):
        return self.__content()

    def __repr__(self):
        return f"'{self.data}'"


def code_table(node: BinTreeNode, tbl={}, path='') -> dict:
    """Создать таблицу кодирования"""
    if node is None:
        return
    code_table(node.left, tbl, path+'0')  # таблица для левого поддерева
    if node.left is None and node.right is None:  # если узел - лист дерева, то
        tbl[node.data] = path  # int(path, base=2)  # сохранить путь в таблице
    code_table(node.right, tbl, path+'1')  # таблица для правого поддерева
    return tbl


def huffman(s: str) -> dict:
    """Кодирование по алгоритму Хаффмана"""
    assert len(s) > 1, "В строке должно быть более одного символа"
    freqs = dict(Counter(s))  # частотный словарь для символов строки
    elems = sorted(freqs, key=freqs.get)  # символы, отсортированные по частоте
    nodes = [BinTreeNode(item) for item in elems]  # узлы дерева
    print(nodes)

    while len(elems) > 1:
        e_l = nodes.pop(0)
        e_r = nodes.pop(0)
        lr_data = e_l.data + e_r.data
        node = BinTreeNode(lr_data, e_l, e_r)  # создать новый узел дерева
        freqs[lr_data] = freqs[e_l.data] + freqs[e_r.data]
        freqs.pop(e_l.data)
        freqs.pop(e_r.data)
        elems = sorted(freqs, key=freqs.get)
        nodes.insert(elems.index(lr_data), node)  # вставить узел в дерево
        # print(elems, end=' ')
        # print(freqs, end=' ')
        print(nodes)

    # print(node)
    print(nodes[0])
    return code_table(nodes[0])


print(__doc__)
s = input("Введите кодируемую строку: ")  # "beep boop beer!"
tbl = huffman(s)
print(f"{tbl = }")
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
