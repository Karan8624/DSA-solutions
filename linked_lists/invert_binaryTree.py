class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 0

        temp = root.left
        root.left = root.right
        root.right = temp 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = TreeNode(8624)
root.left = TreeNode(86)      
root.right = TreeNode(24)
root.right.left = TreeNode(14)   
root.right.right = TreeNode(8) 

print()


