# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        2 solutions: Hashing Approach & Floyd’s Cycle-Finding
        """

        """hashing sol, if null (or repeat) return false, if next of curr not points to prev stores nodes return true"""
        cycleDic = {}