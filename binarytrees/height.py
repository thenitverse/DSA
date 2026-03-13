class BSTNode:
    def __init__(self,val = None):
        self.left = None
        self.right = None
        self.val = val

    def height(self):
        if self.val is None:
            return 0
        
        left_height = 0
        right_height = 0
        if self.left:
            left_height = self.left.height()

        if self.right:
            right_height = self.right.height()

        return max(left_height,right_height) + 1
    
root = BSTNode(10)
root.left = BSTNode(4)
root.left.left = BSTNode(2)
root.right = BSTNode(8)
root.right.right = BSTNode(7)
root.right.right.right = BSTNode(6)

result = root.height()
print(result)