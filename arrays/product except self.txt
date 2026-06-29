#this is a bit hard to explain 
#took me time to think came up with the logic couldnt implement had to claude it almost completely


def product(nums):
    ans = [1]*len(nums)#required to make the answer list 

    for i in range(1,len(nums)):#a linear traversal loop doesnt seem ideal at first but the logic builds up
        ans[i] = ans[i-1]*nums[i-1]

    right = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i] = ans[i]*right
        right = right*nums[i]
        
    return ans

n = [1,2,3,4]
"""
for the first loop it will be [1,1,2,6]
for the second run the loop will start from the end because of the -1 end point 
and -1 as a "stepdown" meaning thst the loop will work ina reverse order
so step by step:
1. [1,1,2,6]>> [1,1,2,6*1] right = right*nums[i] i=3 so right = 1*nums[i] = 4*1=4
2. [1,1,2,6]>>[1,1,2*4,6] = [1,1,8,6] right = 8*3==24
3.[1,1,8,6]>>[1,1*24,8,6] = [1,24,8,6]
"""
print(product(n))

