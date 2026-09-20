class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result  = [] 
        parts = [] 
        nums.sort()
        def build(start, parts):
            result.append(parts[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue   
                parts.append(nums[i])
                build(i + 1, parts)
                parts.remove(nums[i])
        build(0,parts)
        return result
        