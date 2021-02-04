# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        arr = []
        self.preOrderTrav(root, arr)

        minAns = float('inf')
        for i in range(1, len(arr)):
            minAns = min(abs(arr[i]-arr[i-1]), minAns)
            
        return minAns
        
    
    def preOrderTrav(self, root, arr):
        if root.left:
            self.preOrderTrav(root.left, arr)
        
        if root:
            arr.append(root.val)
        
        if root.right:
            self.preOrderTrav(root.right, arr)

        return arr

# testing code
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
arr = []
print(root.minDiffInBST(root))