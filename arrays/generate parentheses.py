def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    answer  = []

    def trace(o,c,curr):
        if o == n and c==n:
            answer.append(curr)
            return answer
        
        if o < n and len(curr)<(n*2):
            trace(o+1,c,curr+"(")

        if o > c and len(curr)<(n*2):
            trace(o,c+1,curr+")")
        
    trace(0,0,"")
    return answer

print(generateParenthesis(n = 8))
    