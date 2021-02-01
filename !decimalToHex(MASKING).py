def toHex(num):
    """
    :type num: int
    :rtype: str
    """

    hexDic = {
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        15:'e',
        16:'f'
    }
    ans = ''
    r = 0 
    if num > 0:
        while num > 0:
            r = num % 16
            if r >= 10:
                ans += hexDic.get(r)
            else:
                ans += str(r)
            num = int(num/16)

        return ans[::-1]
    elif num == 0:
        return '0'
    else:
        num = abs(num)
        while num > 0:
            r = num % 2
            ans += str(r)
            num = int(num/2)
        ans = ans[::-1]
        ans = ans.replace('1','2')
        ans = ans.replace('0','1')
        ans = ans.replace('2','0')
        
        
        print(ans)



#testing
num = -26
print(toHex(num))