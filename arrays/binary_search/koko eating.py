def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    # What does the problem wants us to do?
    """
    1. We are given piles and h
    2. piles is the target and h is the constraint 
    3. We need to figure out the minimum speed in which we can completely empty the pile
       we can only empty one pile at once i.e if the speed k exceeds the pile at any instance 
       we cant access the next pile instantly instead we will finish it for that hour and then 
       move on to the next, This also implies that no matter the speed that no matter the speed
       it will at the very least take time = len(piles) to eat all the bananas
    4. We have to find the MINIMUM 'k' such that it is <= h   
    """
    left = 1 
    right = max(piles)
    
    best = float('inf')
    while left <= right:
        mid = (left+right)//2
        hours = []

        for  n in piles:
            hours.append((n + mid - 1)//mid)
        hour = sum(hours)
        if hour <= h:
            best = min(best,mid)
            right = mid-1
        else:
            left = mid+1
        
            
        hours.clear()


    return best

test  = [3,6,7,11]
h = 8
print(minEatingSpeed(test,h))


#Code logic Explained:-
"""
1. We solve it by a binary search approach.
2. We make a binary seach loops for left = 1 and right = max(piles)
3. The while loop for the binary search will contain variables hours (a list to calculate
    the total hours it took to consume each pile) initialized as an empty list and hour
    a variable to store the total hours it took to finish everything
4. For each value of mid we go throught the entire piles list and create hours list corresponding
    to the index for each pile calculate the ceiling division (n + mid - 1)//mid for each pile
    which gives hours needed to eat that pile at speed mid
5. We sum the piles using hour = sum(hours) if hour is smaller than the constraint h we consider
    it as a valid answer and store it in best = min(best,mid) and then set the search to the first half
6. If hour > h we set the search to the second half 
7. After each mid value fpund we clear hours
8. We go an as it is till we find the minimum and exit the search 

"""

#Dry Run  piles=[3,6,7,11], h=8

"""
left = 1
right = max(piles) = 11
best = infinity

Loop starts:-

Iteration 1:- left = 1, right  = 11:
    mid  = 12/6 = 6
    hours  = [1,1,2,2]
    hour  = 6
    hour < h:
        best  = 6
        right = mid -1 = 5
    
Iteration 2 :- left = 1, right = 5:-
    mid = 3
    hours = [1,2,3,4]
    hour  = 10
    hour > h :-
        left  = mid +1 = 4

Iteration 3 :- left = 4 , right = 5:-
    mid  = 4
    hours = [1,2,2,3]
    hour  = 8
    hour < h:-
    best  = min(4,6) = 4
    right  = 4

iteration 4 left =4, right = 4 :
    mid = (4+4)//2 = 4
    hours = [1,2,2,3]
    hour = 8
    hour <= h:
        best = min(4,4) = 4
        right = 3

"""