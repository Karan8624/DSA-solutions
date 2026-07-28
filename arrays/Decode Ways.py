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

print(numDecodings(s = "226"))

#how does this approach work?
"""
This approach uses dynammic programming to find the solution:
**Initialization**
1. We create dyna list to store the required values the length of this will be len(s)+1 and all elements 0
2. At each instance till (length at that instance) i 
3. The first element in the dyna list is initialized to 1 for its use as the dummy node
4. The first element is the base case in this scenario
5. For the second element in dyna we set it to 0 or 1 depending on the number at index 0 of the 
   string. If its not 0 we set it to 1. If s[0] == '0', dp[1] = 0 meaning no valid decoding exists
**For loop**
1. we check for the element at index (going linearly will be i-1 as i isnt the index directly
   but the length to which we are checking currently)   
2. if the element is non 0 we set the counter to dyna[i-1] 
3. Now we check for the string of numbers double digit if s[i-2:i] >=10  and <=26 we have a valid 
   Char number so we add the dyna[i-2] to dyna[i]

"""
#for the test case that i have used in the code the dyna list comes out to be 
# [1, 1, 2, 3]

"""
dyna[1] is for 2
dyna[2] is for 22
dyna[3] is for 226

"""

print(numDecodings(s = "1011"))
print(numDecodings("01123"))
#the test cases above give the following arrays
"""
[1, 1, 1, 1, 2]
[1, 0, 0, 0, 0, 0]
for the second one you can see how there are no valid combos.
"""