# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def hasCycleFloyd(self, head):
        """
        :type head: ListNode
        :rtype: bool
        2 solutions: Hashing Approach & Floyd’s Cycle-Finding
        """

        """hashing sol, if null (or repeat) return false, if next of curr not points to prev stores nodes return true"""
        sNode = head
        fNode = head

        # fNode.next is not None; check if next exists so that the following .next.next will be None;
        # If no cycle exist; fNode will reach the end of the LL first
        while fNode is not None and sNode is not None and fNode.next is not None:
            sNode = sNode.next
            fNode = fNode.next.next

            if sNode == fNode:
                return True
        
        return False

    def hasCycleBrent(self, head):
        """
        :type head: ListNode
        :rtype: bool
        2 solutions: Hashing Approach & Floyd’s Cycle-Finding
        """
        # edge case
        if head is None:
            return False
        
        sNode = head 
        fNode = head.next

        power = 1
        length = 1

        # finding a loop
        # if there is no loop fNode will end at NULL
        while fNode is not None and sNode != fNode:
            if length == power:
                power *= 2
                length = 0
                sNode = fNode
            fNode = fNode.next
            length += 1
        if fNode is None:
            return False

        sNode = fNode = head
        while length > 0:
            fNode = fNode.next
            length -= 1

        while fNode != sNode:
            fNode = fNode.next
            sNode = sNode.next
        
        return True


# testing
LL = ListNode(3)
LL.next = ListNode(2)
LL.next.next = LL
LL.next.next = ListNode(0)
LL.next.next.next = ListNode(-4)
LL.next.next.next.next = LL.next
print(LL.hasCycleBrent(LL))
'''
comments
- Floyd's cycle detection algo: 1 slow pointer, 1 fast pointer; at different speeds they will meet at a certain point if there exist a cycle
- Brent's cycle detection algo: 1 stationary pointer, 1 fast pointer;
    - fast pointer moves in powers of 2 until loop is found
    - after every power, reset slow pointer to previous value of fast pointer
    - slow n fast pointer == means loop; fast pointer == None == no loop
    - https://www.geeksforgeeks.org/brents-cycle-detection-algorithm/
- hash set works as well; if revisited node you know there is a loop
'''