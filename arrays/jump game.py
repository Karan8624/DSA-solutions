def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #the below approach would have been valid if the choice of steps were absolute, there is a choice to how many steps you can take at instance

    """
    i = 0

    while i < len(nums)-1:
        i += nums[i]
        if nums[i] == 0:
            break

    if i == nums[-1]:
        return True
    else:
        False

    """

    #this is a try to see if i can reach the last index while getting the most out of the ranges
    dist_max = 0
    for i in range(len(nums)):
        if i > dist_max:
            return False
        dist_max = max(dist_max,i+nums[i])#basically the same idea the prev approach used

    return True
print(canJump(nums = [3,2,1,1,4]))

#Explaination:
"""
The first approach failed because we always jumped the max nums

here we limit the number of jumps we can jump if it goes over it its automatically false
all and all we dont have to consider the value of the last element 

"""