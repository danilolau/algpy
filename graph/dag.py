from typing import Any
from ..queue.queue import Queue
from .graph import Graph

class DAG():

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.pred =  {}
        self.shortest = {}

    def topological_sort(self):
        """ This function returns a tuple (is_dag, topological_order) """

        toporder = []
        indegree = {}
        tops = Queue()

        for key, node in self.graph.get_table().items():
            indegree[key] = len(node.parents)
            if len(node.parents) == 0:
                tops.enqueue(node)

        while not tops.is_empty():
            node = tops.dequeue()
            toporder.append(node)
            for child in node.children:
                indegree[child.value] -= 1
                if indegree[child.value] == 0:
                    tops.enqueue(child)

        return (len(toporder)==len(self.graph),toporder)
        

    def dag_shortest_path(self, source: Any):
        """ Update the shortest path from a source, in case it is a DAG Graph."""
        is_dag, toporder = self.topological_sort(self.graph)
        if is_dag:
            self.pred = {}
            self.shortest = {}
            self.shortest[source] = 0
            
            for node in toporder:
                for adj in node.children:
                    short = self.shortest.get(adj.value,float("inf"))
                    cost = self.graph.get_cost(node.value,adj.value)
                    path = self.shortest[node.value] + cost
                    if path < short:
                        self.shortest[adj.value] = path
                        self.pred[adj.value] = node.value
        else:
            raise Exception("It is not a DAG Graph")


    def get_path(self, target: Any):
        """ This function returns the shortest path from target to source. """

        value = target
        path = []

        while (value is not None):
            path.append(value)
            value = self.pred.get(value)

        return path            





    