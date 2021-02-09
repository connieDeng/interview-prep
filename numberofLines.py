def numberOfLines(widths, s):
    """
    :type widths: List[int]
    :type s: str
    :rtype: List[int]
    """

    result = [0] * 2
    lineNum = 1
    width = 0
    
    for i in range(len(s)):
        charWidth = widths[ord(s[i])-ord('a')]
        if charWidth + width > 100:
            lineNum += 1
            width = 0
        width += charWidth

    result[0] = lineNum
    result[1] = width

    print(result)
    return result
        

# testing
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
print(numberOfLines(widths, s))