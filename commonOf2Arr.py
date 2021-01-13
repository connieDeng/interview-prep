def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ansDict = {}
    ansArr = []

    ansDict = dict.fromkeys(nums1, 1)
    nums2 = list(dict.fromkeys(nums2))

    print(ansDict)
    print(nums2)

    for i in range(len(nums2)):
        if ansDict.get(nums2[i]) != None:
            ansArr.append(nums2[i])
    
    # print(ansDict)
    return ansArr


def intersection2(nums1, nums2):
    intersection = []
    for num in nums1:
        if num not in intersection and num in nums2:
            intersection.append(num)
    return intersection

def intersection3(nums1, nums2):
    return set(nums1) & set(nums2)


values1 = [1,2,3,4]
values2 = [2,3]
print(intersection3(values1, values2))

'''
comments
- List: collections of items which can contain elemenets of multiple data types
    - larger memory for easy addition of elements
    - shorter sequence of data items
    - cannot directly handle arithmetic operations
- Array: vector containing items of the same data type -> need to explicitly import a module for declaration
    - more compact in memory size
    - longer sequence of data items
    - can directly handle arithmetic operations

- A dictionary is declared by {}
- Time complexity if dictionaries:
    - insertion; deletion; retrieving -> O(n)

- ansDict = dict.fromkeys(nums1, None) -> array into dict 
- nums2 = list(dict.fromkeys(nums2)) -> array of unique elements
'''