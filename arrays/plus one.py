def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    r = len(digits) -1
     
    while digits[r] == 9:
        digits[r] = 0
        r -= 1

    if r>=0 and digits[r] != 9:
        digits[r] += 1
        return digits
    elif r == -1 and digits[r] == 0:
        digits[0] = 1
        digits = digits + [0]
        return digits
            
print(plusOne(digits = [0]))