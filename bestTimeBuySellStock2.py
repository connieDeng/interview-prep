def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    if prices == None or len(prices) == 0:
        return 0
    else:
        # 
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices [i+1] - prices[i]
        return profit
    
# testing
prices = [1,2,3,4,5]
print(maxProfit(prices))

"""
comments
    - difference from first part of this question is
    - you are buying and selling whenever there is a profit

    - peak valley approach --> simple one pass
"""