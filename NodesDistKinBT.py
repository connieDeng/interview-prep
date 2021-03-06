# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        if root is None or K < 0:
            return
        
        if k == 0:
            ans.append(root.val)
            return


    def distanceKNode(root, target, K):
        if root is None:
            return -1

        if root == target:
            distanceKNode(root, k)
            return 0

# testing code
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)