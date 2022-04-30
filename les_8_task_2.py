# -*- coding: utf-8 -*-
"""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
возвращал список вершин, которые необходимо обойти.
"""


def dijkstra(graph, start):
    """Алгоритм Дейкстры (поиск кратчайшего пути от одной из вершин графа до всех остальных)"""
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    path = [[]] * length
    parent = [-1] * length
    cost[start] = 0
    path[start] = [start]
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    path[i] = path[start] + [i]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return path, cost


print(__doc__)
g = [
     #0  1  2  3  4  5  6  7
     [0, 0, 1, 1, 9, 0, 0, 0],  # 0
     [0, 0, 9, 4, 0, 0, 5, 0],  # 1
     [0, 9, 0, 0, 3, 0, 6, 0],  # 2
     [0, 0, 0, 0, 0, 0, 0, 0],  # 3
     [0, 0, 0, 0, 0, 0, 1, 0],  # 4
     [0, 0, 0, 0, 0, 0, 5, 0],  # 5
     [0, 0, 7, 0, 8, 1, 0, 0],  # 6
     [0, 0, 0, 0, 0, 1, 2, 0],  # 7
]
s = int(input("От какой вершины идти: "))
routes, weights = dijkstra(g, s)
for i, (r, w) in enumerate(zip(routes, weights)):
    print(f"{i}: path={r} (cost={w})")
