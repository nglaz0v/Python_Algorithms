# -*- coding: utf-8 -*-
"""
Написать программу, которая обходит не взвешенный ориентированный граф без
петель, в котором все вершины связаны, по алгоритму поиска в глубину
(Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход
число вершин.
"""

from collections import namedtuple

print(__doc__)
# списки смежности
graph_2a = {
        0: {1, 2},
        1: {0, 2, 3},
        2: {0, 1},
        3: {1},
}
print(graph_2a)
print(3 in graph_2a[1])
print('*'*20)
Vertex = namedtuple("Vertex", ["vertex", "edge"])
graph_2b = []
graph_2b.append([Vertex(1, 2), Vertex(2, 3)])
graph_2b.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_2b.append([Vertex(0, 3), Vertex(1, 2)])
graph_2b.append([Vertex(1, 1)])
print(*graph_2b, sep='\n')
for v in graph_2b[1]:
    if v.vertex == 3:
        print(True)
# print(any([v.vertex == 3 for v in graph_2b[1]]))
print('*'*20)
