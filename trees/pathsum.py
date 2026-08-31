def search( root: Optional[TreeNode], targetSum: int, current_sum :int) -> bool:
    if root.left == None and root.right == None and current_sum ==  targetSum:
        return True 
    left_found = False
    right_found = False
    if root .left:
        left_found =  search(root.left, targetSum, current_sum + root.left.val) 

    if root.right:
        right_found =  search(root.right, targetSum, current_sum + root.right.val) 
    
    return left_found or right_found


def hasPathSum( root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    return  search( root , targetSum , root.val )


