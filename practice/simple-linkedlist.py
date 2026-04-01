class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return new_node.value
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self):
        lis = []
        current = self.head
        while current is not None:
            lis.append(current.value)
            current = current.next
        return lis
    
# 1. Create a new list instance
my_list = Linkedlist()

# 2. Append some values
my_list.append("Shield")
my_list.append("Sword")
my_list.append("Potion")

# 3. Use your to_list method to see the result
result = my_list.to_list()

# 4. Print it out!
print(f"My inventory: {result}")

# 5. Check if it matches what you expect
if result == ["Shield", "Sword", "Potion"]:
    print("Success! The chain is linked correctly.")
else:
    print("Hrmm, something is missing from the chain.")