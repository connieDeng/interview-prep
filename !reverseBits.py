# @param n, an integer
# @return an integer
def reverseBits(n):
    ansStr = n

    if len(ansStr) > 32:
        return -1

    ansInt = 0
    pow = 0
    for i in range(len(ansStr)):
        ansInt += int(ansStr[i]) * (2**pow)
        pow+=1
    
    return ansInt

num = '00000010100101000001111010011100'
print(reverseBits(num))
num = '11111111111111111111111111111101'
print(reverseBits(num))