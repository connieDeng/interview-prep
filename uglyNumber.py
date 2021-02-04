def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False

    num = maxDivide(num, 2)
    num = maxDivide(num, 3)
    num = maxDivide(num, 5)
    return True if num == 1 else False
    

def maxDivide(num, den):
    while num % den == 0:
        num = num/den
    return num

# testing
num = 1
print(isUgly(num))