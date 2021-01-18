def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         skipInd, productSum = 0, 1
#         ansArr = []

#         while skipInd < len(nums):
#                 for i in range(len(nums)):
#                         if i == skipInd:
#                                 pass
#                         else: 
#                                 productSum *= nums[i]
#                 ansArr.append(productSum)
#                 productSum = 1
#                 skipInd+=1
#         print(ansArr)

        lprod = [1] * len(nums)
        rprod = [1] * len(nums)
        ansArr = [1] * len(nums)

        for i in range(1, len(nums)):
                lprod[i] = nums[i-1] * lprod[i-1]
                rprod[len(nums)-i-1] = nums[len(nums)-i] * rprod[len(nums)-i]

        for j in range(len(nums)):
                ansArr[j] = lprod[j] * rprod[j]
        
        return ansArr


nums = [4, 5, 1, 8, 2]
print(productExceptSelf(nums))

"""
comments
        - use product of all val to left and right of the index
        - we created 2 arr, one containing all products to left and one all products to right
        - commutative property of multiplication
        - https://www.youtube.com/watch?v=tSRFtR3pv74
"""