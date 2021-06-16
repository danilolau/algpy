class AVLTree:
    class Node:
        def __init__(self,item) -> None:
            self.item = item
            self.height: int = 1
            self.left_child: self = None
            self.right_child: self = None
            self.parent: self = None

        def clear(self):
            self.parent = None
            self.left_child = None
            self.right_child = None

        def update_height(self):
            left_height = 0
            rigth_height = 0
            if self.left_child is not None:
                left_height = self.left_child.height
            if self.right_child is not None:
                rigth_height = self.right_child.height
            self.height = max(left_height,rigth_height) + 1

        def check_balance(self):
            left_height = 0
            rigth_height = 0
            if self.left_child is not None:
                left_height = self.left_child.height
            if self.right_child is not None:
                rigth_height = self.right_child.height
            return left_height - rigth_height

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
        self.root: self.Node = None
        self.length: int = 0

    def insert(self,item):
        node = self.Node(item)
        self.length += 1
        if self.root is None:
            self.root = node
        else:
            self.__insert_node(self.root,node)

    def __insert_node(self,parent: Node,node: Node):
        if node.item < parent.item:
            if parent.left_child is None:
                parent.left_child = node
                node.parent = parent
            else:
                self.__insert_node(parent.left_child,node)
        else:
            if parent.right_child is None:
                parent.right_child = node
                node.parent = parent
            else:
                self.__insert_node(parent.right_child,node)
        self.__check_balance(parent)

    def __check_balance(self, node: Node):
        node.update_height()
        if node.check_balance() <= -2:
            self.__balance_left(node)
        elif node.check_balance() >= 2:
            self.__balance_right(node)

    def __balance_right(self, node: Node):
        if node.left_child.check_balance() < 0:
            self.__rotate_left(node.left_child)
        self.__rotate_rigth(node)

    def __balance_left(self, node: Node):
        if node.right_child.check_balance() > 0:
            self.__rotate_rigth(node.right_child)
        self.__rotate_left(node)

    def __rotate_left(self, node: Node):
        node_right = node.right_child
        node_parent = node.parent
        node.right_child = node_right.left_child
        node_right.left_child = node
        node_right.parent = node_parent
        node.parent = node_right
        if node.right_child is not None:
            node.right_child.parent = node
        node.update_height()
        node_right.update_height()
        if node_parent is None:
            self.root = node_right
        elif node_right < node_parent:
            node_parent.left_child = node_right
        else:
            node_parent.right_child = node_right

    def __rotate_rigth(self, node: Node):
        node_left = node.left_child
        node_parent = node.parent
        node.left_child = node_left.right_child
        node_left.right_child = node
        node_left.parent = node_parent
        node.parent = node_left
        if node.left_child is not None:
            node.left_child.parent = node
        node.update_height()
        node_left.update_height()
        if node_parent is None:
            self.root = node_left
        elif node_left < node_parent:
            node_parent.left_child = node_left
        else:
            node_parent.right_child = node_left

    def print_tree(self, node: Node, level) -> str:
        if node is None:
            return "[ ]"
        else:
            left_str = self.print_tree(node.left_child, level + 1)
            right_str = self.print_tree(node.right_child, level + 1)
            node_str = "p-{},c-{},h-{}".format(node.parent,node,node.height) + "\n" + level*"\t" + left_str + "\n" + level*"\t" + right_str
            return node_str
        
    def __str__(self) -> str:
        return self.print_tree(self.root,1)

if __name__ == "main":
    import random

    tree = AVLTree()
    seq = random.choices(range(1000), k=15)

    for v in seq:
        tree.insert(v)
        print("Inserting the value {}".format(v))
        print(tree)



