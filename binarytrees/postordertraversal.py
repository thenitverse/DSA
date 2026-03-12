class BSTNode:
    def __init__(self,val = None):
        self.left = None
        self.right = None
        self.val = val
        
    visited =[]
    def postorder(self,visited):
        if self.left:
            self.left.postorder(visited)
            
        if self.right:
            self.right.postorder(visited)

        if self.val is not None:
            visited.append(self.val)

        return visited


root = BSTNode(5)
root.left = BSTNode(4)
root.left.left = BSTNode(3)
root.left.left.left = BSTNode(2)
root.right = BSTNode(6)
root.right.right = BSTNode(7)
root.right.right.right = BSTNode(8)
result = root.postorder([])
print(result)
