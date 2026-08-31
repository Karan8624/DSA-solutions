def dupli(nums):
    seen = set(nums)
    """The first attempt we did include keeping seen as a list and appending the new elements as we go
        but it failed in terms of time consumption this is where the set() keyword came in place 
        This finally  produced a soliution"""
    for n in nums:
        if n in seen:
            return True
    return False
nums = [1,2,3,1,4]
print(dupli(nums))
