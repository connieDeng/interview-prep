def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    ind = 0

    while ind < len(bits)-1:
        if bits[ind] == 1:
            ind += 2
        else:
            ind += 1
        
    return ind == len(bits)-1

# this method is solved through recursion
def isOneBitCharacter2(bits):
    if bits == [0]:
        return True
    if bits == [1,0]:
        return False
    
    if bits[0] == 0:
        return isOneBitCharacter2(bits[1:])
    if bits[0] == 1:
        return isOneBitCharacter2(bits[2:])
# testing code
bitArr = [1, 1, 1, 0]
bitArr2 = [1, 0, 0]
print(isOneBitCharacter2(bitArr))