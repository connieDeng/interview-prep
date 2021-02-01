def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    seen = []
    while n != 1:
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n = int(n/10)
        if sum in seen:
            return False
        else:
            seen.append(sum)
            n = sum
    return True


#testing code
num = 19
print(isHappy(num))