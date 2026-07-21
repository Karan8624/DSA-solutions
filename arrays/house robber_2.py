def rob( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1 = 0
    n2 = 0

    for n in nums[1:]:
        curr1 = max(n+n2,n1)
        n2 = n1
        n1 = curr1

    n1 =0 
    n2 =0
    for n in nums[:len(nums)-1]:
        curr2 = max(n+n2,n1)
        n2 = n1
        n1 = curr2
     

    return max(n1,n2)
test = [2,7,9,3,1]
print(rob(test))