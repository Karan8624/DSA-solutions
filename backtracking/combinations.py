class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        i = 1
        curr_elements = [] 
        ans = []
        def combinations(i , curr_elements , ans , k):
            if len(curr_elements) == k:
                ans.append(curr_elements)
                return 0
            elif len(curr_elements) < k:
                if i <=n:
                    combinations(i +1 , curr_elements,ans , k )
                    combinations(i+1 , curr_elements+ [i] , ans , k)
            else:
                return 0
        combinations(i , curr_elements , ans , k)
        return ans 