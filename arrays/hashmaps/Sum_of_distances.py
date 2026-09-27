class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        seen = {}
        arr = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]].append(i)
            else:
                seen[nums[i]] = [i]
        for n in seen:
            lc = 0
            ls = 0
            rc = len(seen[n]) -1
            rs = sum(seen[n]) - seen[n][0]
            for i in range(len(seen[n])):
                arr[seen[n][i]] = ((seen[n][i] * lc)- ls) + (rs - (seen[n][i] * rc))
                lc += 1
                ls += seen[n][i]
                rc -= 1
                if i + 1 < len(seen[n]) -1:
                    rs -= seen[n][i+1]
                else:
                    rs = 0
        return arr





