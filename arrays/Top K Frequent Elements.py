def topKFrequent(nums,k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] +=1
        else:
            freq[n] = 1
    
    sorted(freq, key=lambda x: freq[x])
    freq = list(freq)
    return freq[0:k]

test = [1,1,1,2,2,3]
print(topKFrequent(test,2))
        

