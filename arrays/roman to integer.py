def rtoi(s):
    master = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans = 0
    for i in range(len(s)):
        if i+1 < len(s) and master[s[i]]<master[s[i+1]]:
            ans -= master[s[i]]
        else:
            ans+= master[s[i]]
    return ans
r = "MCMXCIV"
print(rtoi(r))  