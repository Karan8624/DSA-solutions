def addBinary(a, b):
    alen = len(a) -1
    blen = len(b) -1 
    c = 0
    ans = []
    while alen >=0 or blen >= 0 or c:
        sum = c
        if alen>= 0:
            sum+= int(a[alen])
            alen-=1
        if blen>= 0:
            sum+= int(b[blen])
            blen-=1

        ans.append(sum%2)
        c = sum//2
    return ''.join(map(str, ans[::-1]))

    
        
        

print(addBinary(a = "1010", b = "1011"))
    
