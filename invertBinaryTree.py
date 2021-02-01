# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # always do an base case
        # if there is no right and left children
        if root.left is None and root.right is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

    def PrintTree(self):
        print(self.val)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
#testing
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right = TreeNode(9)
root.right = TreeNode(6)
root.PrintTree()
