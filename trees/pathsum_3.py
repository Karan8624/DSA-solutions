class Solution:
    def search(self , root:Optional[TreeNode], targetSum: int , curr_sum : int, seen : dict) -> int:
        """if curr_sum - targetSum in seen:
            seen[curr_sum] -= 1
            return self.search(root , targetSum , curr_sum, seen , total + 1)
        if root.left:
            if curr_sum + root.left.val not in seen:
                seen[curr_sum + root.left.val] = 1
            else:
                seen[curr_sum + root.left.val] += 1

            self.search(root.left , targetSum , curr_sum + root.left.val , seen, total)

        if root.right:
            if curr_sum + root.right.val not in seen:
                seen[curr_sum + root.right.val] = 1
            else:
                seen[curr_sum + root.right.val] += 1
            self.search(root.right , targetSum , curr_sum + root.right.val , seen , total)"""
        if root:
            curr_sum += root.val
        else:
            return
        if curr_sum - targetSum in seen:
            self.total += seen[curr_sum - targetSum] 
        seen[curr_sum] = seen.get(curr_sum, 0) + 1
        if root.left:
            self.search(root.left, targetSum, curr_sum, seen )
        if root.right:
            self.search(root.right, targetSum, curr_sum, seen)

        seen[curr_sum] -= 1
        


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root :
            self.total = 0
            
            self.search(root , targetSum , 0, {0:1} )
            return self.total
        else:
            return 0

