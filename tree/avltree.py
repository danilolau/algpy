class AVLTree:
    class Node:
        def __init__(self,item) -> None:
            self.item = item
            self.height = 0
            self.left_child = None
            self.right_child = None
            self.parent = None

        def clear(self):
            self.parent = None
            self.left_child = None
            self.right_child = None

        def update_height(self):
            left_height = -1
            rigth_height = -1
            if self.left_child is not None:
                left_height = self.left_child.height
            if self.right_child is not None:
                rigth_height = self.right_child.height
            return max(left_height,rigth_height) + 1

        def check_balance(self):
            left_height = -1
            rigth_height = -1
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
        self.root = None
        self.length = 0

    def insert(self,item):
        node = self.Node(item)
        self.length += 1
        if self.root is None:
            self.root = node
        else:
            self.__insert_node(self.root,node)
            self.root.update_height()
            if self.root.check_balance() <= -2:
                self.rotate_left(self.root)
            elif self.root.check_balance() >= 2:
                self.rotate_right(self.root)

    def __insert_node(self,parent,node):
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

    def rotate_right(self, node: Node):
        pass

    def rotate_left(self, node: Node):
        pass


