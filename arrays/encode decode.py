def encode(strs):
    encoded = ""
    for s in strs:
        encoded = encoded + str(len(s)) + "#" + s
    return encoded

#print(encode(strs = ["hello,world", "hi#there"]))

def decode(s):
    decoded = []
    i =0
    while i < len(s):
        if s[i] == "#" and i > 0 and s[i-1].isdigit():
             n = i-1
             while n>=0 and  s[n].isdigit() :
                n -= 1
             l = int(s[n+1:i])
             decoded.append(s[i+1:i+1+l])
             i = i+1+l
        else:
            i+=1

    return decoded

    """decoded = []
    i =0
    while i<len(s):
        if s[i] =="#":
            j = i
            i += 1
            while s[i] != "#":
                i+=1
            decoded.append(s[j:i])
    return decoded"""

test = "11#hello,world"
print(decode(test))




            
             
            

