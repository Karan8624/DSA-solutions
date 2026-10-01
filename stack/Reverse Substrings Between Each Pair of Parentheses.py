class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        l = []
        for c in s:
            if c == ")":
                l.append([])
                while stack[-1] != "(":
                    l[-1].append(stack.pop())
                if stack[-1] == "(":
                    stack.pop()
                    stack.extend(l[-1])
            else:
                stack.append(c)
        ans = ""
        for c in stack:
            ans+=c
        return ans
