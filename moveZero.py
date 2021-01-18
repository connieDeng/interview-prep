def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    countZero = 0
    i = 0
    while i < len(nums)-countZero:
        print('index is: '+  str(i) + ' limit is: ' + str(len(nums)-countZero)) 
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            countZero += 1
        else:
            i += 1
        # print(nums)
    return

def moveZeroes2(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for num in nums:
        print(num)
        if num == 0:
            nums.remove(num)
            nums.append(num)
        

nums = [0, 1, 0, 1, 0,0]
# moveZeroes(nums)
moveZeroes2(nums)