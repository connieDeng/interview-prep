def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    S = ''
    for i in range(len(paragraph)):
        if paragraph[i].isalpha() or paragraph[i] == ' ':
            S += paragraph[i]
    S = S.lower()
    for i in range(len(banned)):
        S = S.replace(banned[i], '')
    arr = S.split()
    
    countdic = {}
    for i in range(len(arr)):
        if countdic.get(arr[i]) is None:
            countdic[arr[i]] = 1
        else:
            countdic[arr[i]] = countdic[arr[i]] + 1
    ans = ''
    for key in countdic.keys():
        if ans == '' or countdic.get(key) > countdic.get(ans):
            ans = key
    return ans

# testing code
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit","ball"]
print(mostCommonWord(paragraph, banned))