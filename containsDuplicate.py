def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        flag = len(set(nums)) == len(nums) 
        if flag:
            return False
        else:
            return True
    
nums = [1,2,2, 3,4]
print(containsDuplicate(nums))

"""
comments
    - learning of sets; list of unique elements
    - common usecases: comparison of lists
    - useful operations: update, remove (error with non exist index/key), discard (wont error with invalid index/key)
        - intersection, difference, symmetric_difference
"""