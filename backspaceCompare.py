def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    return bool(strTransform(S) == strTransform(T))

def strTransform(S):
    charStack = []
    for i in range(len(S)):
        # if it is not a backspace push it onto stack
        if S[i] != '#':
            charStack.append(S[i])
        #check if stack isn't empty; if it is not empty then we can pop (take away) element
        elif len(charStack) != 0 :
            charStack.pop()
    return charStack

#testing
str1 = "ab##"
str2 = "c#d#"

print(strTransform(str1))
print(strTransform(str2))
print(backspaceCompare(str1, str2))

"""
comments
- used a stack for this problem
- need to check if there are elements in the stack to perform a pop (delete)
"""