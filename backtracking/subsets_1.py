class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        sets = [] 
        parts = []

        def build(i):
            if i ==  len(nums):
                sets.append(parts[:])
                return
            
            parts.append(nums[i])
            build(i+1)
            parts.remove(nums[i])
            build(i+1)
        build(0)

        return sets

        build()
        return sets