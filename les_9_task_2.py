# -*- coding: utf-8 -*-
"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def content(node, k=0):
        s = ''
        if node is None:
            return s
        k += 1
        s += TreeNode.content(node.left, k)
        s += ' '*k*4 + str(node.data) + '\n'
        s += TreeNode.content(node.right, k)
        k -= 1
        return s

    def __str__(self):
        return TreeNode.content(self)

    def __repr__(self):
        return f"'{self.data}'"


print(__doc__)
s = "beep boop beer!"
freqs = dict(Counter(s))
elems = sorted(freqs, key=freqs.get)
leafs = [TreeNode(item) for item in elems]
print(leafs)

while len(elems) > 1:
    e_l = leafs.pop(0)
    e_r = leafs.pop(0)
    node = TreeNode(e_l.data + e_r.data)
    node.left = e_l
    node.right = e_r
    freqs[e_l.data + e_r.data] = freqs[e_l.data] + freqs[e_r.data]
    freqs.pop(e_l.data)
    freqs.pop(e_r.data)
    elems = sorted(freqs, key=freqs.get)
    leafs.insert(elems.index(e_l.data+e_r.data), node)
    print(elems, freqs, leafs)

print(node)
# print(leafs[0])
