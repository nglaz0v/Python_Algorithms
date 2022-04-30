# -*- coding: utf-8 -*-
"""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
возвращал список вершин, которые необходимо обойти.
"""


def dijkstra(graph, start):
    """Алгоритм Дейкстры (поиск кратчайшего пути от одной из вершин графа до всех остальных)"""
    length = len(graph)
    is_visited = [False] * length
    cost = {i: {"path": [], "weight": float('inf')} for i in range(length)}
    parent = [-1] * length
    cost[start]["weight"] = 0
    cost[start]["path"] = [start]
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i]["weight"] > vertex + cost[start]["weight"]:
                    cost[i]["weight"] = vertex + cost[start]["weight"]
                    cost[i]["path"] = cost[start]["path"] + [i]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i]["weight"] and not is_visited[i]:
                min_cost = cost[i]["weight"]
                start = i
    return cost


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
routes = dijkstra(g, s)
for key, val in routes.items():
    print(f"{key}: {val['path']}\t({val['weight']})")
