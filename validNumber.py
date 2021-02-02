# logical method
def isNumber1(s):
    """
    :type s: str
    :rtype: bool
    """
    
    # track what specific char have been seen
    # num, exp, dot
    validDic = { "num": False, "exp": False, "dot": False }
    s = s.strip()
    for i in range(len(s)):
        c = s[i]

        if c.isdigit():
            validDic["num"] = True
        # if there is an exponent; check if there is a prev exponent char or if there are no numbers seem before
        # for instance 'e3' is NOT valid
        elif c == 'e' or c == "E":
            if validDic["exp"] == True or validDic["num"] == False:
                return False
            # if it is the first time e exp = true and seen num = false
            # 1e is NOT valid cus there is no # after the e
            validDic["exp"] = True
            validDic["num"] = False
        # dealing with decimal
        elif c == '.':
            # if we have seen decimal before 
            if validDic["dot"] or validDic["exp"]:
                return False
            validDic["dot"] = True
        elif c == '-' or c == '+':
            if i != 0 and s[i-1] != 'e':
                return False
        else:
            return False
        
    return validDic["num"]

# state machine method
def isNumber2(s):
    """
    :type s: str
    :rtype: bool
    """

# regex method
    
            

# testing 
s = '1E9'
# print(isNumber1(s))
print(isNumber2(s))

'''
comments
- this question has 3 methods of solving;
'''