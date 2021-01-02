def sortedSquares(nums):
    """
    instructions: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
    :type nums: List[int]
    :rtype: List[int]
    """
    #print(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    nums.sort()
    return nums

"""
comments:
- Python sort() also includes arr.sort(key=..., reverse=True)
    key is a function that tells how you want to sort/ do the comparison
    FOR INSTANCE: List1 = [(1,5),(3,3)]
        you can use a key that specifies that you want to sort by the 2nd key
        def sortSecond(val):
            return val[1] #returns 2nd key
        List1.sort(key=sortSecond) #this will sort by the second key so it should return
            [(3,3), (1,5)] --> because 3 < 5
- Python sort() uses TimSort Algo which works in O(n Log n) time --> will implement this sort
"""