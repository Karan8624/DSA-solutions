class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        sets = [] 
        parts = []

        def build():
            if len(parts) == len(nums):
                sets.append(parts[:])

            for n in nums:
                if n not in parts:
                    parts.append(n)
                    build()
                    parts.remove(n)

        build()
        return sets