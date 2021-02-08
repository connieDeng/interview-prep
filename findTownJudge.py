def findJudge(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    # base case if only one person
    if N == 1:
        return 1

    # this is adj matrix
    # graph = { x: [] for x in range(1, N + 1) }    
    # people who trust them; trusting "in"
    indegrees = { x: 0 for x in range(1, N + 1) }
    # who they trust
    outdegrees = { x: 0 for x in range(1, N + 1) }

    # count in and out degrees
    for u, v in trust:
        outdegrees[u] += 1
        indegrees[v] += 1

    print(indegrees)
    for i in range(1,N+1):
        if indegrees[i] == N-1 and outdegrees[i] == 0:
            return i
    
    return -1
# following is first solution has a time limited exceeded
    # for pairs in trust:
    #     trustMatrix[pairs[1]-1][pairs[0]-1] = 1

    # print(trustMatrix)

    # for i in range(N):
    #     if sum(trustMatrix[i]) == N-1:
    #         for j in range(N):
    #             judgeTrust += trustMatrix[j][i]

    #     if sum(trustMatrix[i]) == N-1 and judgeTrust == 0:
    #         return i+1
    # return -1

#testing
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(findJudge(N, trust))