def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    carrOver = 0

    endA = len(a)-1
    endB = len(b)-1
    ans = str("")

    print(endA)
    print(endB)

    while endA >= 0 or endB >= 0:
        sum = carrOver
        if endA >= 0:
            sum += int(a[endA])
            endA -= 1

        if endB >= 0:
            sum += int(b[endB])
            endB -= 1

        ans += str(int(sum%2))
        carrOver = int(sum/2)
    if carrOver > 0:
        ans += str(1)

    print(ans)
    return ans[::-1]

#testing
B1 = '111'
B2 = '1'

print(addBinary(B1,B2))

"""
Comments:
- be careful if types in this question int, str, floats
- since binary is a base-2 numeral system, %2 and /2 are common
- %2 finds the value to be appended to the string while /2 calculates the value of the carry
    - 1 + 1 = 2;
        2 % 2 == 0 --> number to be appended to answer
        2 / 2 == 1 --> carry calc
"""