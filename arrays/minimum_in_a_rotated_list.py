def mininRotated(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1
    return nums[left]

n = [2, 2, 2, 0, 1]
print(mininRotated(n))
