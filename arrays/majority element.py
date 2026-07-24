def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = {}
    for n in nums:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] = 1

    return max(seen, key= seen.get)

print(majorityElement(nums = [6,6,6,7,7]))