def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    #This is a valid attempt but failed on time complexity since its a O(n2) approach
    """for i in range(len(gas)):
        fuel = gas[i] - cost[i]
        mark = i 
        while  fuel >= 0:
            if i == len(gas)-1:
                i = 0
            else:
                i+=1
            fuel += gas[i] - cost[i]
            if fuel <0:
                break
            else:
                if mark == i:
                    return mark
                continue

    return -1"""
    # 2nd attempt failed too 
    """i = 0
    while i < len(gas):
        fuel = gas[i] - cost[i]
        mark = i
        
        while fuel >= 0:
            if i == len(gas)-1:
                i = 0
            else:
                i += 1
            fuel += gas[i] - cost[i]
            if fuel < 0:
                break
            if mark == i:
                return mark
        i = i + 1"""

    #this is the greedy approach for the problem the above brute force does work but fails on time 
    total  = 0
    curr = 0
    j = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i] # the total amount keeps getting updated
        curr += gas[i] - cost[i] # this gets reset if we encounter a lower than 0 current fuel

        if curr < 0:
            j = i+1
            curr = 0

    if total > 0:
        return j
    else:
        return -1


    
        


print(canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))


            

    