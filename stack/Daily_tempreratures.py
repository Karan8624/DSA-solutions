def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    #this does work but failed on time complexity
    answer  = [0]*len(temperatures)

    left = 0
    right = 1

    while left<len(temperatures)-1:
        right = left+1
        while right<len(temperatures)-1 and temperatures[right] <= temperatures[left] :
            right+=1
        if temperatures[right] <= temperatures[left]:
            left+=1
        else:
            answer[left] = right -left
            left += 1
    return answer

def dailyTemperatures2(temperatures):
    stack = []
    answer = [0]*len(temperatures) #create an answer array for answer
    for i in range(len(temperatures)):
        if len(stack)>0 and temperatures[i]> temperatures[stack[-1]]:
            """
            if the last temperatures recorded is smaller than the encountered one start assigning
            the elements in the stack hteir distance from that day and pop each time until you empty 
            the stack   
            """
            while len(stack)>0 and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
        stack.append(i) #append everytime 
    return answer

test = [73,74,75,71,69,72,76,73]
print(dailyTemperatures2(test))
        

#Dry run :- temperatures = [73, 74, 71, 75]

"""
stack = [], answer = [0,0,0,0]

i=0: stack empty → skip while
     stack.append(0) → stack=[0]

i=1: temps[1]=74 > temps[stack[-1]]=temps[0]=73 
     while stack and temps[0]<74:
         answer[0] = 1-0 = 1
         stack.pop() → stack=[]
     stack.append(1) → stack=[1]

i=2: temps[2]=71 > temps[1]=74? NO  (skip)
     stack.append(2) → stack=[1,2]

i=3: temps[3] = 75 > temps[2] = 75 Yes
     answer[2] = 1
     stack.pop()  = stack[1]
     answer[1] = 2
     stack.pop() = stack[]


"""
    
    