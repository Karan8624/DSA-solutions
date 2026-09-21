class Solution:
    def search(self, root, targetSum, current_sum, ans, result):
        if root.left == None and root.right == None:
            if current_sum == targetSum:
                result.append(ans)
            return 
        if root.left:
            self.search(root.left, targetSum, current_sum + root.left.val, ans + [root.left.val], result)
        if root.right:
            self.search(root.right, targetSum, current_sum + root.right.val, ans + [root.right.val], result)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.search(root, targetSum, root.val, [root.val], result)
        return result