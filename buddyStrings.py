def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """

    # check if strings len are same
    if len(A) != len(B):
        return False
    
    # going to dive into this following section a bit more:
    #   so if the strings are equal --> covering the cases "abab" vs "ab"
    #   2 x abab == True and 2 x ab == False
    #   IF it's only ab --> the set and length will be the same meaning no repeat
    #   if there is a repeat of pattern the length of the set (unique elements) will be less
    #   if there exists a repeat of pattern a swap will still make the strings the same resulting in true
    if A == B:
        if len(set(A)) < len(A):
            return True
        else:
            return False
        
    diff = []
    # setting up diff arr
    for i in range(len(A)):
        if A[i] != B[i]:
            diff.append(i)
    # checking if a single swap would fix
    if (len(diff) == 2 and A[diff[0]] == B[diff[1]] and 
            A[diff[1]] == B[diff[0]]):
        return True
    else:
        return False
                
#testing
A = "a"
B = "a"
print(buddyStrings(A, B))