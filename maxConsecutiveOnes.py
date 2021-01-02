def findMaxConsecutiveOnes(nums):
    """
    instructions: Given a binary array, find the maximum number of consecutive 1s in this array.
    :type nums: List[int]
    :rtype: int
    """
    maxCnt = 0
    holdCnt = 0
    i = 0
    
    while i < len(nums):
        if nums[i] == 1 and i != len(nums)-1:
            holdCnt+=1
            i+=1
        else:
            if nums[i] == 1:
                holdCnt+=1
            if maxCnt < holdCnt:
                maxCnt = holdCnt
            holdCnt = 0
            i+=1
    
    return maxCnt

"""
comments as you are attempting this question:
- since you only check the length of conseq 0s if the next number isn't 1,
    the last set of 1's arent checked because there isn't a 0 at the end
    of the array
"""