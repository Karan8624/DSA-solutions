class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max,right_max)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        
        if max(left_max-right_max,right_max - left_max)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)