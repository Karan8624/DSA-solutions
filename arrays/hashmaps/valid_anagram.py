def anagram(t,s):
    uni = {}
    for c in s:
        if c in uni:
            uni[c] = uni[c]+1
        else:
            uni[c] = 1

    for c in t:
        if c in uni:
            uni[c] = uni[c]-1

    for k in uni:
        if uni[k]!=0:
            return False
    return True

s = "karan"
t = "nara"

print(anagram(t,s))