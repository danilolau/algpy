class Queue:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
        def __repr__(self):
            return str(self.item)

    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, item):
        node = self.Node(item)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        data = None
        if self.first is not None:
            data = self.first.item
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
        return data

    def is_empty(self):
        empty = False
        if self.first is None:
            empty = True
        return empty

    def __repr__(self):
        nodes = []
        pointer = self.first
        nodes.append("->")
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("->")
            pointer = pointer.next
        return "".join(nodes)
