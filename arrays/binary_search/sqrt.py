def mySqrt(x: int) -> int:
    left  = 0
    right  = x
    if x <=1:
        return x
    while left < right:
        mid = (left + right)//2
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            right = mid-1
        else:
            left = mid+1

    if x - right * right < x - (right-1)*(right-1) and x-right*right >=0:
        return right
    else:
        return right-1

print(mySqrt(x= 9))