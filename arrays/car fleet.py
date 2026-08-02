def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """

    #Whats the problem exactly????
    """
    We have to find the number of fleets that will be formed for a set of cars with speeds(speed list)
    and distance (position list), The speed and distance for the cars at the corresponding addresses

    Fleets means how many sets of cars will arrive at each instance if they can overtake
    If there a re three cars with distance = [2,4,7] and speed  = [1,5,2] target = 12

    The car at position 7 will block the car behind it from reaching the target as it will take
    longer for it to rach there compared to car at position 4 which inspite of having higher speed 
    cant over take it, So the car at position 4 catches upto 7 and then proceeds to move with it 
    arriving at the same time as 7, where as the car at position 2 with speed 1 will never catch
    upto both of them resulting it to arrive after both of them 
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



position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
target = 12
print(carFleet(target,position,speed))

# Codes Explaination:
"""
1. we sort the positions of cars in descending order while zipping them with their respective speeds
2. This creates ps(positions sorted) in the format [[position(sorted),speed]]
3. we use the ps(position sorted list) to make the time list using a loop and formula target-p[0])/float(p[1])
4. The time list will have the time it takes for each vehicle to reach the target arranged in the descending 
    order according to their position
5.  The cars in front will block the cars behind them inspite of having a lesser time to reach the target
6 . In this case while traversing throught the time linearly whenever we encounter a greater time 
    its a fleet 
"""

#Dry run: position = [10, 8, 0, 5, 3] , speed = [2, 4, 1, 1, 3] , target = 12

"""
flrrt = 0 
max time = 0
ps = (10, 2), (8, 4), (5, 1), (3, 3) , (0,1)
time  =  [1.0, 1.0, 7.0, 3.0, 12.0]

traversing throught time :-
at iteration 1:-
maxTime  = 1
fleet += 1 = 1

iteration2 skip time < max

iteration3 time> max:
fleeet  = 2
max time  =7

iteration4 skip

iteration 5 time > max(17)
maxtime = 12
fleet = 3
"""

