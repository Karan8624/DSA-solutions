def longestCommonPrefix(strs):

    ans = ""
    if not strs:
        return ans
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):
        check = strs[0][i]
        for s in range(len(strs)):
            if i >= len(strs[s]) or check != strs[s][i]:
                return ans 
            if s == len(strs) - 1:
                ans += strs[s][i]
    return ans  
s = ["flower","flow","flight"]

print(longestCommonPrefix(s))
                
                
