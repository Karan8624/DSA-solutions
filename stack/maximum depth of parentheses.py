class Solution:
    def maxDepth(self, s: str) -> int:
        op = 0
        counter = -9999

        for c in s:
            if c == "(":
                op += 1
            if c == ")":
                op-= 1
            counter = max(counter , op)

        return counter
