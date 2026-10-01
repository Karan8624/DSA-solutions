class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        left = 0
        right  = len(nums)-1
        while left < right:
            mid = (left+right)//2
            
            if target  > nums[mid-1] and target <= nums[mid]:
                return mid
            elif target  >= nums[mid] and target <= nums[mid+1]:
                return mid +1 
            elif target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid+1
            
        return len(nums)