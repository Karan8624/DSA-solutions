class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        s = sum(nums)
        temp = (s + target )//2
        if (s + target) %2 == 1 or target <  (-1)*s:
            return 0

        dp = [[0]*(temp+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1    
        for i in range(1 , len(nums)+1):
            for j in range(temp+1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i - 1]] 
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[-1][-1]

        