def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    #set up string for testing, removing white space, symbols that aren't characters
    #strip(), replace(), isalpha(), lower(), isalnum
    #to get the ASCII code of a character use ord

    s = s.replace(' ', '')
    testStr = ''
    for i in range(len(s)):
        if s[i].isalnum() == True:
            testStr += s[i]
    
    if(len(testStr) == 0 or len(testStr) == 1):
        return True
    else:
        testStr = testStr.lower()
        firstind = 0
        lastind = len(testStr)-1

        while(firstind <= lastind):
            if(testStr[firstind] == testStr[lastind]):
                firstind+=1
                lastind-=1
            else:
                return False
        return True


example = '0P'
print(isPalindrome(example))

"""
comments
- differences between alpha and alphanumeric
    - alpha: only letters
    - alphanumeric: letters and numbers, not symbols
    - 2 line answer
        def isPalindrome(self, s: str) -> bool:
            filter_s = "".join(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
            return filter_s == filter_s[::-1]

    - fast answer
        def isPalindrome(self, s: str) -> bool:
            newS=""
            for char in s:
                if char.isalnum():
                    newS+=char.lower()
            
            
            def rec(s,left,right):
                if left>=right:
                    return True
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
                return rec(s,left,right)
            
            s=newS
            return rec(s,0,len(s)-1)
"""