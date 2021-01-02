def findNumbers(nums):

    """
    instruction: Given an array nums of integers, return how many of them contain an even number of digits.
    :type nums: List[int]
    :rtype: int
    """
        
    digArr = []
    numOfEvenDigNum = 0

    for index in range (len(nums)):
        #val will hold val of index num
        val = nums[index]

        #numOfDig will hold number of digits
        numOfDig = 0

        while val >= 1:
            numOfDig += 1
            val = val/10
        
        digArr.append(numOfDig)

    print(digArr)

    #count num that have even numbers
    for i in range (len(digArr)):
        if digArr[i] % 2 == 0:
            numOfEvenDigNum+=1

    return numOfEvenDigNum
    
"""
comments:
there is a difference between the following for loops: for i in arr AND for i in range (len(arr))
    the first, you are unable to access a certain index, it's useful to apply something to each index such as print(i) - print all
    the second, you are able to access and change a certain index - you have more control
"""