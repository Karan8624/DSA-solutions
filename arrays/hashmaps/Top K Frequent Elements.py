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
    

    return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]

test = [1,1,1,2,2,3]
print(topKFrequent(test,2))
        

