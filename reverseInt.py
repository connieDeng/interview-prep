def reverseInt(x):
    isNeg = False

    if x < 0:
        isNeg = True
    
    x = abs(x)
    ans = 0
    #place value holder
    place = 0
    deconstructedInt = []

    while x > 0:
        deconstructedInt.append(x % 10)
        place+=1
        x = int(x/10)

    # print(deconstructedInt)
    # print(place)
    j = 0
    while j < len(deconstructedInt): #desconsturctedInt incrementing
        for i in range(place, 0, -1): #num places going backwards
                ans += deconstructedInt[j] * (10 ** (i-1))
                j+=1
    
    if ans <= (-2**31)  or ans >= (2**31)-1:
        return 0

    if isNeg == True:
        ans = ans * -1

 

    return ans

"""
comments:
    - biggest takeaway: reversing list --> list[<start>:<stop>:<step>]
    - this question dealt with int overflow (-2**31) <= x <= (2**31)-1 which were these values for a 32-bit signed num
    - another person's answer:
            def reverse(self, x: int) -> int:
                if x > 0:
                    r = int(str(x)[::-1]) #converted int into string arr and reverses it list[<start>:<stop>:<step>]
                    return 0 if r > 2147483647 else r
                else:
                    r = -1 * int(str(abs(x))[::-1])
                    return 0 if r < -2147483647 else r
    
"""