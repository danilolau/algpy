from typing import Any
from .graph import Graph
from enum import Enum
from ..linkedlist.lklist import LinkedList

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class DFSearch:
    class Node:
        def __init__(self, value: Graph.Node) -> None:
            self.d: int= 0
            self.f: int = 0
            self.color: Color = Color.WHITE
            self.parent: self = None
            self.value: Graph.Node = value
            self.children: list[self] = []

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.forest: dict[Any, self.Node] = {}
        self.time = 0
        self.tree_edges: list = []
        self.back_edges: list = []
        self.forward_edges: list = []
        self.cross_edges: list = []
        self.topological_sort = LinkedList()
        self.roots: list = []
        for key, node in graph.get_table().items():
            self.forest[key] = self.Node(node)

    def get_node(self, key) -> Node:
        return self.forest[key]

    def dfs(self):
        for key, node in self.forest.items():
            if node.color == Color.WHITE:
                self.roots.append(node)
                self.__dfs(node)

    def __dfs(self, node: Node):
        self.time += 1
        node.d = self.time
        node.color = Color.GRAY
        key = node.value.value
        for adj in self.graph.get_node(key).children:
            adj_node = self.get_node(adj.value)
            edge = (key, adj.value)
            if adj_node.color == Color.WHITE:
                adj_node.parent = node
                node.children.append(adj_node)
                self.tree_edges.append(edge)
                self.__dfs(adj_node)
            elif adj_node.color == Color.GRAY:
                self.back_edges.append(edge)
            elif adj_node.color == Color.BLACK:
                if adj_node.f > node.d:
                    self.forward_edges.append(edge)
                else:
                    self.cross_edges.append(edge)
        node.color = Color.BLACK
        self.time += 1
        node.f = self.time
        self.topological_sort.push(node)
        

