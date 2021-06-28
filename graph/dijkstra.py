from sys import path
from typing import Any
from .graph import Graph
from heapq import heappop, heappush

def dijkstra( graph: Graph, source: Any):
    pred = dict()
    shortest = dict()
    q = set()
    h = []
    shortest[source] = 0
    heappush(h,(shortest[source],source))
    while h:
        _ , value = heappop(h)
        if value not in q:
            q.add(value)
            for adj in graph.get_node(value).children:
                cost = graph.get_cost(value,adj.value)
                short = shortest.get(adj.value,float("inf"))
                path = shortest[value] + cost
                if path < short:
                    shortest[adj.value] = path
                    pred[adj.value] = value
                    heappush(h,(shortest[adj.value],adj.value))
    return pred, shortest


    