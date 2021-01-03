def insertionSort(nums):
    """
    Implementation of Insertion Sort
    Complexity time: O()
    
    Your arr is split into a sorted and unsorted part. continuously compare key to elements before and 
    insert into the correct place
    """
    if len(nums) == 1 or len(nums) == 0:
        return nums
    elif len(nums) == 2:
        if nums[1] < nums[0]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    else:
        for i in range(1, len(nums)):
            key_val = nums[i]

            while nums[i-1] > key_val and i > 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
    return nums           
