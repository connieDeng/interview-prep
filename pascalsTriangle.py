def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.split()
        print(s)

        if(len(s) != 0):
            return len(s[-1])
        else:
            return 0

