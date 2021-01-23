def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    #edge case
    if len(nums) == 0:
        return -1
    
    left = 0
    right = len(nums)-1
    
    # keep left ind before right ind
    while(left <= right):
        mid = int(left + (right-left)/2)
        # target found
        if nums[mid] == target:
            return mid
        # if target is < nums[mid] then move right 
        elif nums[mid] > target:
            right = mid - 1
        # if target is > nums[mid] then move left 
        else:
            left = mid + 1
    return -1

# testing
nums = [-1,0,3,5,9,12]
target = 2

print(search(nums, target))
    