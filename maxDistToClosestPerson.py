def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """

    prev_seat = None
    dist = float('-inf')

    for i in range(len(seats)):
        if seats[i] == 1:
            if prev_seat is None:
                dist = i
            else:
                dist = max(dist, int(i - prev_seat)/2)
            prev_seat = i

    # need to check if the person sat at the very end
    return max(dist, len(seats) - 1 - prev_seat)
                
           
     
    
# testing code
seats = [1,0,0]
# seats = [1,0]
print(maxDistToClosest(seats))