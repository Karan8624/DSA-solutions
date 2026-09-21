class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max,right_max)
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        diameter_here = left_max + right_max
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(diameter_here, left_diameter, right_diameter)
