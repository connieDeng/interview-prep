def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = 0
        
    #if each number is a 9 it will reach here
    digits.insert(0, 1)
    return digits
