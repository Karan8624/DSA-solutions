def numDecodings( s):
    """
    :type s: str
    :rtype: int
    """
    #this seems right but fails on test cases
    """
    counter = 0
    for i in range(len(s)):
        if int(s[i]) != 0 and int(s[i-1]) != 0:
            counter+=1
        if i>0 and int(s[i-1:i])>=10 and int(s[i-1:i])<23:
            counter+=1
        
    return counter
    """

    dyna = [0]*len(s) + [0]
    dyna[0] = 1


    if int(s[0]) == 0:
        dyna[1] = 0
    else:
        dyna[1] = 1

    for i in range(2,len(s)+1):
        if int(s[i-1]) != 0:
            dyna[i] += dyna[i-1]

        if int(s[i-2:i]) >= 10  and int(s[i-2:i]) <= 26:
            dyna[i] += dyna[i-2]
    return dyna[-1]

print(numDecodings(s = "1011101"))

#how does this approach work?
"""
1. First we initiated the dynamic 

"""