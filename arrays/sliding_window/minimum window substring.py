def min_window(s,t):
    win = ""
    count = 0
    left =0
    right = 0
    target = {}
    flag = len(t)
    best = float('inf')
    for a in t:
        if a in target:
            target[a] +=1
        else:
            target[a]  = 1
    
    while right < len(s):
        if s[right] in target:
            if target[s[right]]>0:
                flag -= 1
            target[s[right]] -=1
        right += 1

        while flag == 0:
            curr  = right -left+1
            best = min(best,curr)
            if curr == best:
                r = right
                l = left
            if s[left] in target:
                target[s[left]] +=1
                if target[s[left]]>0:
                    flag += 1
            left += 1
            
    return s[l:r]

st = "a"
t = "a"
print(min_window(st,t))
            
