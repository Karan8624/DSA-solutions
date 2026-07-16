def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    best  = -1
    flag = 0
    for i in range(0,len(s)-2):
        left = i
        right = len(s)-1
        while left < right:
            l = left
            r  = right
            r2 = right
            while s[l] == s[r2]:
                if l >= r2:
                    best =  min(best,r2 - l)
                l += 1
                r2 -= 1
            
