def jump(nums):
    #this didnt work properly.
    """
    distance = 0

    limit  = len(nums)-1
    c = 0
    i = 0

    while distance +i + nums[i] < limit:
        c+= 1
        i+=1
    return c+1
    """
    limit  = 0
    end = 0
    reach =0
    c = 0
    for i in range(len(nums)-1):
        reach = max(reach , nums[i] + 1) #simmilar to distance in the previous approach
        if i == end:
            c+=1
            end = reach
    return c


print(jump(nums = [2,3,1,1,4]))


        


