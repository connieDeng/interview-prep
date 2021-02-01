def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dynamic programming question
    # bottom of processing solve for 0, 1 ,2, n...

    # first case
    if nums is None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    # dynamic programming array
    # dp arr will hold the max amount you can rob to the i index
    dp = [0] * len(nums)
    
    # only one house to rob from so most you can rob is the value of that one house
    dp[0] = nums[0]
    
    # when you have 2 houses, max $ you can rob is the max of the two houses
    dp[1] = max(nums[0], nums[1])

    # for more indexes; start from 2 because first 2 cases are solved above
    for i in range(2, len(dp)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    print(dp)
    return max(dp)

# testing
nums = [1,2,3,1]
print(rob(nums))