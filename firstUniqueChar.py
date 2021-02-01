def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    arr = [0] * 26
    for i in range(len(s)):
        arr[ord(s[i]) - 97] += 1
    
    for i in range(len(s)):
        if arr[ord(s[i]) - 97] == 1:
            return i

    return -1

#testing 
S = ''
print(firstUniqChar(S))