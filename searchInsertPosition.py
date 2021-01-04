def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    i = 0
    
    if target > nums[-1]: #get the last element of arr
        return len(nums)
    else:
        while i < len(nums):
            if(target > nums[i]):
                i+=1
            elif(target == nums[i]):
                return i
            else:
                return i