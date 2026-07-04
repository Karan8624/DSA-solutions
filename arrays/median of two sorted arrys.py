nums1 = [1,3]
nums2 = [2,4]

nums = sorted(nums1 + nums2)
if len(nums)%2 ==0:
    mid1 = (len(nums)+1)//2
    mid2 = mid1-1
    print((nums[mid1]+nums[mid2])/2)
else:
    mid = (len(nums))//2
    print(nums[mid])



