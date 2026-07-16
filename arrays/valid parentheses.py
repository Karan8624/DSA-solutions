def validParentheses(s):
    o = set(["(","[","{"])
    cl = set([")","]","}"])
    oc = {")":"(","]":"[","}":"{"}
    flag = []
    i = 0
    for c in s:
        if c in o:
            flag.append(c)
            continue
        elif c in cl:
            if len(flag)==0 or oc[c] == flag[-1]:
                flag.pop()
            else:
                return False
                
            
            
    return True



test = "{]}"

print(validParentheses(test))
        
