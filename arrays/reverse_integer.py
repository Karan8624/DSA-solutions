def reverse(x: int) -> int:
    sign = 1
    if x<0 :
        sign = -1

    rev = str(abs(x))
    rev = int(rev[::-1])
    if rev > -2 ** 31 and rev < 2**31:
        return rev*sign
    else:
        return 0

print(reverse(86247))
