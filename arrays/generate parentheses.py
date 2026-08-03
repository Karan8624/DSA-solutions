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

print(generateParenthesis(n = 2))

#Explaination:-
"""
1. The code uses recursion logic to create valid pairs
2. Each time we call the function with different values check if we have both open and close counter
   are equal to n if yes we add the curr to the answer
3. if o < c then we add "(" to curr and call trace again with a incremented o(open) counter or viceversa

"""

#Dry Run:- n=2

"""
1. call trace(0,0,""):
     call trace(1,0,"("):
        call trace(2,0,"(("):
            call trace (2,1,"(()"):
                call trace(2,2,"(())"): append("(())"
        call trace(1,1,"()"):
            call trace (2,1,"()("):
                call trace(2,2,"()()"): append ("()()")


"""
    