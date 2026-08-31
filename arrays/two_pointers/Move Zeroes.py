def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    fast = 0
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            temp = nums[fast]
            nums[fast] = nums[slow]
            nums[slow] = temp 
            slow+=1
    return nums

print(moveZeroes(nums = [0,1,0,3,12]))