def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start = 1
    end = n
    target = 0
    while start <= end:
        # //2 is floor division
        mid = start + (end-start)//2
        if isBadVersion(mid):
            target = mid
            end = mid - 1
        else:
            start = mid + 1
    return target

def isBadVersion(n):
    if n == 4:
        return True
    else:
        return False
# testing 
n = 5
bad = 4
print(firstBadVersion(n))