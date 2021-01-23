def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    
    stack = []
    for i in range(len(ops)):
        if ops[i] not in ['x', '+', 'D', 'C']:
            stack.append(int(ops[i]))
            print(stack)
        elif ops[i] == 'C':
            stack.pop()
            print(stack)
        elif ops[i] == 'D':
            stack.append(stack[-1] * 2)
            print(stack)
        elif ops[i] == '+':
            stack.append(stack[-1] + stack[-2])
            print(stack)
    
    return sum(stack)

#testing
ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))