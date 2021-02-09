# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        # stack
        ans, stack = [], []

        # place root into stack
        if root:
            stack.append((root, root.val, [root.val]))

        # while stack is not empty
        while stack:
            node, currSum, vals = stack.pop()
            # this is ans condition where root - leaf target is found
            if node.left is None and node.right is None and currSum == targetSum:
                ans.append(vals)
            
            # if answer isn't found recurse left and right trees
            if node.right is not None:
                stack.append((node.right, currSum+node.right.val, vals + [node.right.val]))
                
            if node.left is not None:
                stack.append((node.left, currSum+node.left.val, vals + [node.left.val]))
        
        return(ans)


'''
comments
- current.copy()
    - gotta google what this does
    - how to make a temp copy in python
    - stack appending multiple elements into "one" element
'''
# testing
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(root.pathSum(root, 22))