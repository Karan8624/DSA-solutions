def maxsub(nums):
    curr = nums[0]
    best = nums[0]

    for n in nums[1:]:
        curr = max(n,curr+n)
        best = max(curr,best)
    return best 

num = [1,2,-2,3,5-10,11]

print(maxsub(num)) 

