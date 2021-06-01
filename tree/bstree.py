import random

class BinarySearchTree:
    class Node:
        def __init__(self,item) -> None:
            self.item = item
            self.left_child = None
            self.right_child = None
            self.parent = None

        def clear(self):
            self.parent = None
            self.left_child = None
            self.right_child = None

        def __repr__(self) -> str:
            return str(self.item)

        def __eq__(self, other) -> bool:
            return self.item == other.item

        def __ne__(self, other) -> bool:
            return self.item != other.item

        def __gt__(self,other) -> bool:
            return self.item > other.item

        def __ge__(self, other) -> bool:
            return self.item >= other.item

        def __lt__(self,other) -> bool:
            return self.item < other.item
        
        def __le__(self,other) -> bool:
            return self.item <= other.item

        def __hash__(self) -> int:
            return hash(self.item)

    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def get_random_node(self) -> Node:
        count = random.choice(range(self.length))
        elem, count = self.__visit(self.root, count)
        return elem

    def __visit(self, node: Node, count):

        if node is None:
            return (None, count)

        if count == 0:
            return (node, count)
        
        if node.left_child is not None:
            count -= 1
            elem, count = self.__visit(node.left_child,count)
            if elem is not None:
                return (elem, count)

        if node.right_child is not None:
            count -= 1
            elem, count = self.__visit(node.right_child,count)
            if elem is not None:
                return (elem, count)

        return (None,count)
    
    def add(self,item):
        node = self.Node(item)
        self.length += 1
        if self.root is None:
            self.root = node
        else:
            self.__add_node(self.root,node)
        
    def __add_node(self,parent,node):
        if node.item < parent.item:
            if parent.left_child is None:
                parent.left_child = node
                node.parent = parent
            else:
                self.__add_node(parent.left_child,node)
        else:
            if parent.right_child is None:
                parent.right_child = node
                node.parent = parent
            else:
                self.__add_node(parent.right_child,node)


    def add_random(self, item):
        child = self.Node(item)
        if self.root is None:
            self.root = child
        else:
            self.__add_random(self.root,child)

    def __add_random(self, node: Node, child: Node):
        if node.left_child is None:
            node.left_child = child
            child.parent = node
        elif node.right_child is None:
            node.right_child = child
            child.parent = node
        else:
            c = random.choice([0,1])
            if c == 0:
                self.__add_random(node.left_child,child)
            else:
                self.__add_random(node.right_child,child)

    def remove(self, item):
        node = self.find(item)
        print("removing the node: {}".format(node))
        if node is not None:
            self.length -= 1
            return self.__rm_node(node)

    def __rm_node(self,node: Node):
        successor = self.successor(node)
        print("selected the successor {}".format(successor))
        if self.is_leaf(node):
            if node.parent is not None:
                if node < node.parent:
                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
            else:
                self.root = None
        elif node.left_child is None:
            node.right_child.parent = node.parent
            if node.parent is not None:
                if node < node.parent:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child
            else:
                self.root = node.right_child
        elif node.right_child is None:
            node.left_child.parent = node.parent
            if node.parent is not None:
                if node < node.parent:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child
            else:
                self.root = node.left_child
        else:
            successor = self.__rm_node(successor)
            successor.parent = node.parent
            successor.right_child = node.right_child
            successor.left_child = node.left_child
            if successor.right_child is not None:
                successor.right_child.parent = successor
            if successor.left_child is not None:
                successor.left_child.parent = successor
            if successor.parent is not None:
                if successor < successor.parent:
                    successor.parent.left_child = successor
                else:
                    successor.parent.right_child = successor
            else:
                self.root = successor

        node.clear()

        return node

    def is_leaf(self, node: Node):
        is_l = False
        if node.left_child is None and node.right_child is None:
            is_l = True
        return is_l

    def find(self, item):
        found = False
        node = self.root
        while not found and node is not None:
            if node.item == item:
                found = True
            elif item < node.item:
                node = node.left_child
            elif item > node.item:
                node = node.right_child
        return node
        

    def successor(self, node: Node) -> Node:
        if node.left_child is not None and node.right_child is not None:
            return self.min_node(node.right_child)
        elif node.left_child is not None:
            return node.left_child
        elif node.right_child is not None:
            return node.right_child
        

    def min_node(self,node: Node) -> Node:
        if node.left_child is None:
            return node
        else:
            return self.min_node(node.left_child)
    
    def max_node(self,node: Node) -> Node:
        if node.right_child is None:
            return node
        else:
            return self.max_node(node.right_child)

    def print_tree(self, node, level) -> str:
        if node is None:
            return "[ ]"
        else:
            left_str = self.print_tree(node.left_child, level + 1)
            right_str = self.print_tree(node.right_child, level + 1)
            node_str = "{},{}".format(node.parent,node) + "\n" + level*"\t" + left_str + "\n" + level*"\t" + right_str
            return node_str
        
    def __str__(self) -> str:
        return self.print_tree(self.root,1)


