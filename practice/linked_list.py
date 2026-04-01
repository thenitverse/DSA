class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def get_last_node(head):
    if head is None:
        return None
    while head:
        if head.next is None:
            return head.value
        if head.next is not None:
            head = head.next


# 1. Create the nodes
node1 = Node("sun")
node2 = Node("moon")
node3 = Node("stars")

# 2. Link them together
node1.next = node2
node2.next = node3
node3.next = None

# 3. Call your function with the head (node1)
result = get_last_node(node1)
print(result) 
