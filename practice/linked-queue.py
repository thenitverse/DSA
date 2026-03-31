class QueueNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self,value):
        new_node = QueueNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None
        n_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.length-=1
        return n_node.value
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def size(self):
        return self.length
    def to_list(self):
        val = []
        current = self.head
        while current is not None:
            val.append(current.value)
            current = current.next

        return val

q = linkedqueue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue())  # A
print(q.peek())     # B
print(q.to_list())  # ["B"]
print(q.size())     # 1
print(q.is_empty()) # False