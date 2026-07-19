def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """

    left = 1
    right = max(piles)
    count = 0
    best = float('inf')
    while left <= right:
        mid = (left+right)//2
        i = 0
        hours = []

        for  n in piles:
            hours.append((n + mid - 1)//mid)
        hour = sum(hours)
        if hour <= h:
            best = min(best,mid)
            right = mid-1
        else:
            left = mid+1
        
            
        count = 0
        hours.clear()


    return best

test  = [3,6,7,11]
h = 8
print(minEatingSpeed(test,h))

                

    