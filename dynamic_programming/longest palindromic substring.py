def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    best  = ""
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    for i in range(len(s)):
        
        odd = expand(s,i,i)
        even = expand(s,i,i+1)
        if len(odd) > len(best):
            best = odd
        if len(even) > len(best):
            best  = even
    return best

print(longestPalindrome(s = "babad"))

#the Logic(didnt add a failed case because nothing worked other than this till now):

"""
The nested function "expand" plays an important role in this program. what it does?
    The expand function will expand both ways from left and right we (set those
    at each index) until either one of the pointers reach their ends OR there is a mismatch between
    the elements at index left and right, hence checking for palindrome each time it expands and
    returning the string.

we use expand function to detect 2 times at each index, The reason we do it twice:-
    As expand function expands both sides it will work differently for odd and even lengthed 
    palindromes heres why explained with a dry run 

    dry run:-
        Case --> s = "abaccaa"


        (without the even case)
            at i=0 fails 
            at i=1 (a==a) expands left and right hits left returns "aba
            as we go on we wont find another palindrome and "aba" will be considered to be the best

        Case:
        (with the even case)
            at i=0  fails 
            at i=1: odd =(a==a) expands left and right hits left returns "aba
                     even  = fails 
                     best = aba
            at i=2: odd = fails 
                    even = fails
            at i=3: odd = a==c fails
                    even = (c==c) expands (a==a) expands (b==a) fails
                    best = acca
            no more palindromes found after that 

    The dry case gives an example why the answer might be difficult for the calculation of odd and
    even palindromic substrings, The differnce that causes this is the difference in the number of 
    middle elements , odd has 1 middle element and even has 2 
"""