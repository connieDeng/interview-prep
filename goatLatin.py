def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    ans = []
    wordArr = S.split()
    print(wordArr)
    # strAns = ''
    
    for i in range(len(wordArr)):
        if wordArr[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            ans.append(wordArr[i] + 'ma' + str('a')*(i+1))
        else:
            firstL = wordArr[i][0]
            # print(firstL)
            ans.append(wordArr[i][1:] + firstL + 'ma' + str('a')*(i+1))
    strAns = ' '.join(ans)
    print(strAns)
            

#testing 
S = "zzGPuClvxA XYbNe"
print(toGoatLatin(S))