def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    """greater = {}

    for i in range(len(nums2)-1):
        if nums2[i] in nums1:
            if nums2[i] >= nums2[i+1]:
                greater[nums2[i]] = -1
            else:
                greater[nums2[i]] = nums2[i+1]
    greater[nums2[-1]] = -1
    ans = []
    for n in nums1:
        ans.append(greater[n])
    return ans"""

    """greater = {}
    stack = []

    for n in nums2:
        if len(stack) == 0:
            stack.append(n)

        while stack[-1] <= n:
            continue
        
        

    ans = []
    for n in nums1:
        ans.append(greater[n])

    
    return ans"""

    greater = {}
    stack = []
    ans = []
    for n in nums2:
        while stack  and stack[-1]<n:
            greater[stack.pop()] = n      
        stack.append(n)
    while stack:
        greater[stack.pop()] = -1

    for n in nums1:
        ans.append(greater[n])
    return ans
            

    
    

print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
            
    






