def threesome(nums):
    ans = []
    nums.sort()
    """
    SO WHATS THE LOGIC FOR THIS?
    unlike the two sum we have a different approach here. in 2sum we used the 'seen' approach but doing that here is quite 
    inefficient instead we use something simmilar to binary search:
    
    THE LOGIC :
    1. The numbers are first sorted, necessary since we cannot do it without slightly immitating binary search
    2. We use 't' to traverse through the range(0,len(nums)), t is used as the index
    3. For each 't' in list we initialize 'left' = t+1 and right to the last index
    4. We create 'check' and store the value of check = nums[t] + nums[left] + nums[right] in it.]
    5. Think about it this way if check is +ve it means we have to decrease a number to get zero or if its -ve we need 
       to increase the numbers. 
    6. Since the list is converted to ascending order we can get a grater or smaller value by just incrementing left or
       decrementing right
    7. to do the above we use the binary search approach so we use the while left<right loop 
    
    THE ERROR HANDLING:
    1. We dont want to repeat itself since it will give the same answer twice which is not valid 
        soln:- just skip running the loop further using continue
    2. Simmilarly to case1 if we get a repeated number while checking at left and right we also need to skip that part
        soln:- increment and decrement left and right until a new element is found
    """

    for t in range(0,len(nums)):
        left = t+1
        right = len(nums)-1
        if t< len(nums) and nums[t] == nums[t-1]:#Case 1
            continue 
        while left<right:
            check = nums[t] + nums[left] + nums[right]
            if check == 0:
                ans.append([nums[t],nums[left],nums[right]])
                left += 1
                right -= 1
                #Case 2
                while left <  right and nums[left] ==  nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
            elif check<0:
                left+=1
            else:
                right -= 1
    return ans
n = [-1,0,1,2,-1,-4]
print(threesome(n))
      
            
