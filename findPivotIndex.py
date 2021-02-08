def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # left sum starts at 0
    # right sum starts as sum of all numbers after 1; find equal point
    leftsum, rightsum = 0, sum(nums[1:])
    
    for i in range(len(nums)-1):
        if leftsum == rightsum:
            return i
        leftsum += nums[i]
        rightsum -= nums[i+1]
    
    # print(leftsum))
    # print(rightsum)

    if leftsum == rightsum:
        return i + 1  
    else:
        return -1

# testing
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))