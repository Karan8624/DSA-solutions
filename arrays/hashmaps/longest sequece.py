def longestConsecutive(nums: List[int]) -> int:
    search = set(nums)
    seen  = set()
    best = -float('inf')
    if nums == []:
        return 0
    count = 1
    for n in nums:
        if n in seen or n-1 in search:
            continue
        else:
            c  = n + 1
            while c in search:
                c+=1
                count += 1
        seen.add(n)
        best = max(best,count)
        count = 1

    return best

print(longestConsecutive([100,4,200,1,3,2]))

