def countSubstrings( s):
    """
    :type s: str
    :rtype: int
    """

    def expand(s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count+=1    
            left -= 1
            right += 1
        return count
    ans = 0
    for i in range(len(s)):
        odd = expand(s,i,i)
        even = expand(s,i,i+1)
        ans += odd + even
    return ans

print(countSubstrings(s = "abc"))

    



    