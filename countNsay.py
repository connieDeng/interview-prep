# Returns n'th term in 
# look-and-say sequence 
def countAndSay(n): 
    s = '1'
    # 
    while n > 1:
        currStr = ''
        i = 0
        while i < len(s):
            count = 1
            while((i+1) < len(s) and s[i] == s[i+1]):
                print('count should increment')
                count += 1
                i+=1
            currStr += str(count) + s[i]
            i+=1
        s = currStr
        n -= 1
    return s
# Driver Code 
N = 4
print(countAndSay(N)) 