class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lans = ListNode()

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                lans.next = l1
                l1 = l1.next
                lans = lans.next
            elif l2.val < l1.val:
                lans.next = l2
                l2 = l2.next
                lans = lans.next

        while l1 != None and l2 == None:
            lans.next = l1
            l1 = l1.next
            lans = lans.next

        while l2 != None and l1 == None:
            lans.next = l2
            l2 = l2.next
            lans = lans.next
