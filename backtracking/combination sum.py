class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        curr_elements  = []
        curr_sum = 0
        ans = []
        length = len(candidates)
        i = 0
        def summing(i  , target , curr_elements , ans , curr_sum):
            if curr_sum == target:
                ans.append(curr_elements)
                return 0
            elif curr_sum < target:

                summing(i , target , curr_elements + [candidates[i]] , ans, curr_sum + candidates[i])
                if i < length -1:
                    summing(i+1, target , curr_elements, ans , curr_sum)
                

            else:
                return 0

        
        summing(i,target,curr_elements , ans , curr_sum)

        return ans
        
