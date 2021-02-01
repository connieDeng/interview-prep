# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    sum = 0
    transformTreeUtil(root, sum)

def transformTreeUtil(root, sum):
    if root == None:
        return 
    
    transformTreeUtil(root.right, sum)

    sum += sum + root.data
    root.data = sum - root.data

    transformTreeUtil(root.left, sum)


#testing
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)