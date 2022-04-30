# -*- coding: utf-8 -*-
"""
Написать программу, которая обходит невзвешенный ориентированный граф без
петель, в котором все вершины связаны, по алгоритму поиска в глубину
(Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход
число вершин.
"""


def generate_graph(n):
    """
    Сгенерировать невзвешенный ориентированный граф без петель, в котором все
    вершины связаны

    :param n: число вершин графа
    :return: граф в виде списка смежности
    """
    fullset = {i for i in range(n)}
    graph = {i: fullset - {i} for i in range(n)}
    return graph


def dfs(graph, start, visited=None):
    """Обход графа по алгоритму поиска в глубину (Depth-First Search)"""
    if visited is None:
        visited = []  # set()
    if start not in set(visited):
        visited.append(start)  # visited.add(start)
    # print(start)
    for cur in graph[start] - set(visited):
        dfs(graph, cur, visited)
    return visited


print(__doc__)
g = {
     0: {1, 3, 4},
     1: {2, 5},
     2: {1, 6},
     3: {1, 5, 7},
     4: {2, 6},
     5: {6},
     6: {5},
     7: {6}
}
g = generate_graph(8)
print(g)

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
print(dfs(graph, '0'))
print(dfs(g, 0))


import random
def graph_gen(vertex):
    vert = []
    graph = dict()
    for i in range(vertex):
        vert.append(i)

    for i in vert:
        vert_ch = random.choices(vert, k = random.randint(1, vertex))
        vert_ch = set(vert_ch)
        vert_ch.discard(i)
        graph.update([(str(i), vert_ch)])

    return graph

print(graph_gen(10))
