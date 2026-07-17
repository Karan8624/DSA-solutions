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
    answer = [0]*len(temperatures)
    for i in range(len(temperatures)):
        if len(stack)>0 and temperatures[i]> temperatures[stack[-1]]:
            while len(stack)>0 and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
        stack.append(i)
    return answer
        

            

test = [73,74,75,71,69,72,76,73]
print(dailyTemperatures2(test))
        
        
    
    