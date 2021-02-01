def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    numDic = {}
    for i in range(len(nums)):
        # current is the "key" which you are finding another duplicate for
        current = nums[i]
        print(i)
        print(numDic.get(current))
        if(numDic.get(current) != None and (i - numDic.get(current)) <= k):            
            return True
        else:
            numDic[current] = i
        print(numDic)
        print("\n")
    return False


    
#testing
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))