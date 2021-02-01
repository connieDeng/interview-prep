def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(len(A)):
        L = 0
        R = len(A[i])-1
        # print(A[i])
        # print(A[i][L])
        # print(A[i][R])
        while L <= R:

            print('before ' + str(A[i]))
            A[i][L], A[i][R] = A[i][R], A[i][L]
            print('after ' + str(A[i]))
            A[i][L], A[i][R] =  int(not(A[i][L])), int(not(A[i][R]))
            print('inverted ' + str(A[i]))
            L+=1
            R-=1

    return A
            

#testing
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(A))

"""
comments
- another way to invert a bit is to do 1 - (but)
    - if 0: 1 - 0 = 1
    - if 1: 1 - 1 = 0
"""