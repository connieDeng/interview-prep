def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    count = 0
    while N > 0:
        if isVal(N):
            count += 1
        N -=1

    return count

def isVal(N):
    rotate_themselves = [0,1,8]
    rotate_valid = [2,5,6,9]
    rotate_invalid = [3,4,7]
    
    themselves_cnt = 0
    valid_cnt = 0
    digit_cnt = 0

    while N > 0:
        if N % 10 in rotate_themselves:
            themselves_cnt += 1
        elif N % 10 in rotate_valid:
            valid_cnt += 1
        elif N % 10 in rotate_invalid:
            return False

        N = int(N/10)
        digit_cnt += 1
    
    # print(digit_cnt)
    # print(themselves_cnt)
    if digit_cnt == themselves_cnt:
        return False
    
    return True

    
# testing
N = 857
print(isVal(0))
