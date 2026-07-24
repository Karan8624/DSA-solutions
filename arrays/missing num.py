def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()

    for i in range(0,len(nums)):
        if i == nums[i]:
            continue
        else:
            break
    if i == (len(nums)-1):
        return i+1
    else:
        return i


print(missingNumber(nums = [3,0,1]))