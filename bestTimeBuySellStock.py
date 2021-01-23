def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxNum = 0 
    minNum = float('inf')

    for i in range(len(prices)):
        if prices[i] < minNum:
            minNum = prices[i]
        else:
            maxNum = max(maxNum, prices[i]-minNum)
    
    return maxNum
        
#testing
prices = [7,6,4,3,1]
print(maxProfit(prices))