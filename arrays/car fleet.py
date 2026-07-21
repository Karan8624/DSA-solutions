def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    
    time = []
    ps = sorted(zip(position,speed),reverse=True)

    for p in ps:
        time.append((target-p[0])/float(p[1]))

    fleets = 0
    max_time = 0
    for t in time:
        if t > max_time:
            fleets += 1
            max_time = t
    return fleets



p = [6,8]
s = [3,2]
t = 10

print(carFleet(t,p,s))