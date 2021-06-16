class LinkedList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
        def __repr__(self):
            return str(self.item)

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        node = self.Node(item)
        self.push_node(node)

    def push_node(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, item):
        node = self.Node(item)
        self.append_node(node)
        
    def append_node(self,node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def append_list(self,itens):
        for item in itens:
            self.append(item)
        
    def remove(self,item):
        if self.head.item == item:
            self.head = self.head.next
            return True
        
        pointer = self.head
        
        while pointer.next != self.tail:
            if pointer.next.item == item:
                pointer.next = pointer.next.next
                return True
            pointer = pointer.next
            
        if self.tail.item == item:
            self.tail = pointer
            self.tail.next = None
            return True
        
        return False
        
    def __repr__(self):
        nodes = []
        pointer = self.head
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)
