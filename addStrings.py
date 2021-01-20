def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    carrOver = 0

    end1 = len(num1)-1
    end2 = len(num2)-1
    ans = str("")
    # return type is a string

    while end1 >= 0 or end2 >= 0:
        #this will include the carry over value
        #for instance if carry = 1 that will be included in this temp sum
        tempSum = carrOver

        #if num1 has a digit add it
        if end1 >= 0:
            tempSum += int(num1[end1])
            #remember to decrement
            end1 -= 1

        #same situation with second number
        if end2 >= 0:
            tempSum += int(num2[end2])
            end2 -= 1

        #in the case 8+8 = 16, we need to make carry = 1 and value to append to string 6
        ans += str(tempSum%10) # this should return 6
        carrOver = int(tempSum/10) #this will calculate the write carry 
        tempSum = 0

    if carrOver == 1:
        ans += str(1)

    return ans[::-1]



num1 = ""
num2 = "78"
print(addStrings(num1, num2))

"""
Comments
- extremely similar to addBinary; make tempSump = carryOver to deal with carry overs
- for value to append and carr over use % and / to do the calculations
"""