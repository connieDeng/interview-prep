def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    prev = len(arr)

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
           arr.insert(i+1, 0)

    aft = len(arr)

    diff = aft - prev

    for i in range(diff):
        arr.pop()