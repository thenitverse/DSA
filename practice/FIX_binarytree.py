class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_tree_report(root):
    # Base case: an empty tree has no values and 0 height
    if root is None:
        return ([], 0)

    # Recursive step: get reports from children
    left_values, left_height = get_tree_report(root.left)
    right_values, right_height = get_tree_report(root.right)

    # Inorder: Left -> Root -> Right
    values = left_values + [root.value] + right_values
    
    # Height: 1 (for the current node) + the tallest subtree
    height = 1 + max(left_height, right_height)

    return (values, height)


# This part allows you to run the file directly in VS Code
if __name__ == "__main__":
    # Manually building a small tree:
    #    10
    #   /  \
    #  5    15
    my_tree = TreeNode(10, TreeNode(5), TreeNode(15))
    
    report_values, tree_height = get_tree_report(my_tree)
    
    print(f"Inorder Traversal: {report_values}")
    print(f"Tree Height: {tree_height}")