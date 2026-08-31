def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    #first attempt that passed but failed on 10 test cases 


    """check = [False]*len(s) 
    k = 0
    flag = 0
    for i in range(len(s)):
        for w in wordDict:
            if w == s[k:k+len(w)]:
                k = k+len(w)
                if k == len(s):
                    return True
            else:
                continue
    return False"""
    # What was the Problem with this??
    """
    The problem here is that its a greedy approach whwnever it finds a string that 
    matches the condition if w == s[k:k+len(w)]: it locks it in which migh work 
    for most of the test cases but fails when there is a better suited one present after it 
    """
    #Example of failiue:-
    """
    s = "cars"
    wordDict = ["car","ca","rs"]
    """
    #Reason:
    """
    This case shows how "car" is suited for index 0 to 2 so it locks it in 
    now it searches for the lonely S but guess what it fails and returns false
    Whereas if it picked "ca" instead and "rs" after that it would have passed .
    """

    #**Main Code stars here**
    check = [False]*(len(s) + 1)
    check[0] = True
    for i in range(1,len(s)+1):
        for w in wordDict:
            if i>= len(w) and check[i-len(w)] and s[i-len(w):i] == w:
                check[i] = True
                break
    return check[len(s)]


print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))


