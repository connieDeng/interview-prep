def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    binary = ''
    while num > 0:
        binary += str(1-(num % 2))
        num = int(num/2)
    return(int(binary[::-1],2))
    
# testing
num = 2
print(findComplement(num))