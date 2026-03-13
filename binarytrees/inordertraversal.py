class BSTNode:
    def __init__(self,val = None):
        self.left = None
        self.right = None
        self.val = val
    visited = []
    def inorder(self,visited):
        if self.left:
            self.left.inorder(visited)

        if self.val is not None:
            visited.append(self.val)

        if self.right:
            self.right.inorder(visited)

        return visited

root = BSTNode(5)
root.left = BSTNode(4)
root.left.left = BSTNode(3)
root.right = BSTNode(6)
root.right.right = BSTNode(7)

result = root.inorder([])
print(result)
