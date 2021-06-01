class DoublyLinkedList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            self.prev = None
            
        def __repr__(self):
            return str(self.item)

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = self.Node(item)
        self.append_node(node)
        
    def append_node(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
    def append_list(self,itens):
        for item in itens:
            self.append(item)
        
    def remove_node(self,node: Node):
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return True
                
    def remove(self,item):        
        pointer = self.head
        while pointer is not None:
            if item == pointer.item:
                return self.remove_node(pointer)
            pointer = pointer.next
        return False
    
    def __repr__(self):
        nodes = []
        pointer = self.head
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)