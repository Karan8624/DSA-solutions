def rob( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1 = 0
    n2 = 0

    for n in nums:
        curr = max(n+n2,n1)
        n2 = n1
        n1 = curr

    return n1
test = [2,7,9,3,1]
print(rob(test))

"""
Test run
initialization n1 =0 ,n2 =0

loop 
Run-1 (n1=0,n2=0,n=nums[0]=2)

curr = max(2+0,0) = 2
n2 = n1= 0
n1 = curr = 2

Run-2 (n1 = 2, n2 =0 , curr = 2, n= 7)
curr = max(9,2) = 9
n1 = 9
n2 = 2

Run-3 (n1 = 9,n2=2,n = 9, curr = 9 )

curr= max(11,9)= 11
n2 = 9
n1 = 11

run-4 (n1=11, n2= 9 , n= 3, curr =11)
curr = max(11,11) = 11
n2 = n1  = 11
n1 = curr

run -5 (n1=11,n2=11,n=1,curr =11)
curr = (12,11) =12


"""