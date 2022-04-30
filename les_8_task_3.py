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

import random


def generate_graph(n):
    """
    Сгенерировать невзвешенный ориентированный граф без петель, в котором все
    вершины связаны

    :param n: число вершин графа
    :return: граф в виде списка смежности
    """
    graph = {}
    vertices = [i for i in range(n)]
    for i in vertices:
        chosen = random.choices(vertices, k=random.randint(1, n))
        graph[i] = set(chosen) - {i}
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
g = generate_graph(8)
print(g)
print(dfs(g, 0))
