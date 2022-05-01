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


def generate_graph(n: int) -> dict:
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


def dfs(graph: dict, start: int, visited=[]) -> list:
    """
    Обход графа по алгоритму поиска в глубину (Depth-First Search)

    :param graph: граф в виде списка смежности
    :param start: начальная вершина
    :param visited: список посещённых вершин
    :return: маршрут обхода графа
    """
    if start not in set(visited):
        visited.append(start)
    # print(start)
    for current in graph[start] - set(visited):
        dfs(graph, current, visited)
    return visited


print(__doc__)
n = 8
graph = generate_graph(n)
print(f"{graph = }")
start = 0
route = dfs(graph, start)
print(f"{route = }")
