def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    isVal = False
    validArr = [] #they name this variable stack

    i = 0
    
    if len(s) % 2 != 0:
        return False
    else:
        while i in range(len(s)):
            if s[i] != ']' and s[i] != '}' and s[i] != ')': # if not equal closing brackets
                validArr.append(s[i])
                i+=1
            else: 
                if len(validArr) > 0 and s[i] == ']' and validArr.pop() == '[':
                    print(validArr)
                    i+=1
                elif len(validArr) > 0 and s[i] == ')' and validArr.pop() == '(':
                    print(validArr)
                    i+=1
                elif len(validArr) > 0 and s[i] == '}' and validArr.pop() == '{':
                    print(validArr)
                    i+=1
                else:
                    return False
    
    return True if len(validArr) == 0 else False

"""
comments:
    - their solution uses a hash map, improving run time lookup - same stack implementation
    - mapping = {")": "(", "}": "{", "]": "["}
    - if mapping[char] != top_element:
    - https://leetcode.com/problems/valid-parentheses/solution/
"""