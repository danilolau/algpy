class Stack:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
        def __repr__(self):
            return str(self.item)
    
    def __init__(self):
        self.head = None

    def push(self,item):
        node = self.Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def pop(self):
        data = None
        if self.head is not None:
            data = self.head.item
            self.head = self.head.next
        return data

    def is_empty(self):
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty

    def __repr__(self):
        nodes = []
        pointer = self.head
        nodes.append("-->")
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)