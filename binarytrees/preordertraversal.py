class BSTNode:
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val
    visited = []    
    def preorder(self,visited):
        if self.val is not None:
            visited.append(self.val)

        if self.left:
            self.left.preorder(visited)

        if self.right:
            self.right.preorder(visited)

        return visited
  # building a tree  
root = BSTNode(4)
root.left = BSTNode(3)
root.right = BSTNode(6)
root.left.left = BSTNode(2)
root.right.right = BSTNode(8)

# call preorder
result = root.preorder([])
print(result)
