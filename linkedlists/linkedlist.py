class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node


    def delete_head(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next


    def display(self):
        temp = self.head
        while temp:
            print((temp.data),end = " ")
            temp = temp.next
        print("None")

    def delete_tail(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

ist = linkedlist()
ist.insert_head(10)
ist.insert_tail(9)
ist.insert_head(7)
ist.delete_head()
ist.delete_tail()

ist.display()