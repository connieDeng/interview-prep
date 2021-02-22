def largeGroupPositions(s):
    """
    :type s: str
    :rtype: List[List[int]]
    """
    ans = []
    i = 0
    arr = []
    counter = 1
    
    for i in range(1, len(s)):
        # print(str(s[i]) + '==' + str(s[i-1]))
        if s[i] == s[i-1]:
            counter += 1
        elif s[i] != s[i-1] or i == len(s)-1:
            if counter >= 3:
                arr.append(i-counter)
                arr.append(i-1)
                ans.append(arr)
                arr = []
                counter = 1
            else:
                counter = 1
            i+=1
    if counter >= 3:
        arr.append(len(s)-counter)
        arr.append(len(s)-1)
        ans.append(arr)

    return ans

# testing
s = "abc"
print(largeGroupPositions(s))