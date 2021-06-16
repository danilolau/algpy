import random
from typing import Any
from ..queue.queue import Queue

class Graph:
    class Node:
        def __init__(self, value):
            self.value: Any = value
            self.children: list[self] = []
            self.parents: list[self] = []

        def add_child(self,node):
            self.children.append(node)

        def add_parent(self,node):
            self.parents.append(node)

        def __eq__(self, other: object) -> bool:
            return self.value == other.value

        def __ne__(self, other: object) -> bool:
            return self.value != other.value

        def __hash__(self):
            return hash(self.value)

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self.__table: dict = {}
        self.__cost: dict = {}
        self.__root: self = None

    def is_empty(self):
        return len(self.__table)==0

    def add_path(self,a, b, cost):
        node_a = self.__table.get(a,None)
        node_b = self.__table.get(b,None)
        if node_a is None:
            node_a = self.Node(a)
            self.__table[a] = node_a
        if node_b is None:
            node_b = self.Node(b)
            self.__table[b] = node_b
        node_a.add_child(node_b)
        node_b.add_parent(node_a)
        self.__cost[(a,b)] = cost

    def remove_node(self,value):
        node = self.get_node(value)
        if node is not None:
            for child in node.children:
                child.parents.remove(node)
            for parent in node.parents:
                parent.children.remove(node)
            node.children = []
            node.parents = []
            self.__table.pop(value)
        return node

    def set_node(self,value):
        node = self.__table.get(value,None)
        if node is None:
            node = self.Node(value)
            self.__table[value] = node

    def get_node(self,value) -> Node:
        return self.__table.get(value,None)

    def get_table(self):
        return self.__table

    def search_dfs(self,a,b):
        node = self.get_node(a)
        path = []
        marked = {}
        found = self.__dfs(node,b,path,marked)
        path.reverse()
        return (found,path)
        
    def __dfs(self,node: Node,target: Any,path: list,marked: dict):
        if node.value == target:
            path.append(node)
            return True
        marked[node.value] = True
        for child in node.children:
            if not marked.get(child.value,False):
                r = self.__dfs(child,target,path,marked)
                if r:
                    path.append(node)
                    return True
        return False

    def search_bfs(self,a,b):
        if a == b:
            return [a]
        path = {}
        queue = Queue()
        queue.enqueue(self.get_node(a))
        path[a] = [a]
        while not queue.is_empty():
            node = queue.dequeue()
            for c in node.children:
                path = path.get(c.value,None)
                if path is None:
                    path[c.value] = path[node.value].copy().append(c.value)
                    if c.value == b:
                        return path[c.value]
                    queue.enqueue(c)
        return []

    def __repr__(self):
        nodes = []
        for item in self.__table.values():
            nodes.append(str(item) + " --> " + str(item.children) + "\n")
        return "".join(nodes)


