class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max,right_max)

root = TreeNode(8624)
root.left = TreeNode(86)      
root.right = TreeNode(24)
root.right.left = TreeNode(14)   
root.right.right = TreeNode(8) 

print(Solution().maxDepth(root)) 