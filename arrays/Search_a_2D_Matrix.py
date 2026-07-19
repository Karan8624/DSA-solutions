def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    left  = 0
    right = len(matrix)-1

    while left<=right:
        if left >= len(matrix):
            return False
        mid = (left+right)//2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            right = mid-1
        else:
            left = mid+1
    if target >= matrix[left][-1]:
        row = matrix[left]
    else:
        row = matrix[right]
    r = len(row) -1
    l = 0
    while l<=r:
        mid = (l+r)//2
        if row[mid] == target:
            return True
        elif row[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return False



    

    

test = [[1,2,5,7],[10,11,16,20],[23,30,34,60]]
t = 3
print(searchMatrix(test,t))
        
    