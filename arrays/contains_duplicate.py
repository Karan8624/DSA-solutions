def dupli(nums):
    seen = set(nums)
    for n in nums:
        if n in seen:
            return True
    return False
nums = [1,2,3,1,4]
print(dupli(nums))
