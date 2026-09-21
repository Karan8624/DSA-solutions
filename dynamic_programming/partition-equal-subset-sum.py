class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        possible = {0}
        total = sum(nums)
        if total %2  == 1:
            return False
        half = total//2
        for n in nums:
            temp = []
            for sums in possible:
                temp.append(n+sums)
            for s in temp:
                possible.add(s)
            if half in possible:
                return True 

        return False