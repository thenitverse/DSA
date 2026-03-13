class BSTNode:
    def __init__(self,val = None):
        self.left = None
        self.right = None
        self.val = val

    def exists(self,val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)
        if val > self.val:
            if self.right is  None:
                return False
            return self.right.exists(val)
        
tree = BSTNode(10)
tree.left = BSTNode(5)
tree.right = BSTNode(15)

print(tree.exists(10))  
print(tree.exists(5))   
print(tree.exists(15))  
print(tree.exists(7))  