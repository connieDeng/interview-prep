class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # now we need to check the heigh of left and right subtrees
        # only return tree if the differece between them is <= 1 &
        # both left and right subtrees are balanced (recursion)

        # always check if root node exists
        # return true because leetcode said so
        if root == None:
            return True
        else:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            print(str(leftHeight) + ' and ' + str(rightHeight))

            # abs value (difference) is <= 1 and you need to check that for
            # each node
            # print(abs(leftHeight-rightHeight))
            if (abs(leftHeight-rightHeight) <= 1 and self.isBalanced(root.left) and 
                self.isBalanced(root.right)):
                return True
            return False

    def getHeight(self, node):
        # again check if root node exists
        # when node is null it DOES NOT add to the height == 0 
        if node == None:
            return 0
        # return the max of left and right heights and add 1 too keep adding height
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

#testing
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(4)
print(tree.isBalanced(tree))

"""
comments
- to get height you do a recursion while adding 1
"""