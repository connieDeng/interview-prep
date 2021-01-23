# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if root == None:
            return paths
        #helper DFS function
        self.dfs(root, "", paths)
        return paths

    # clarification: path = single path
    # paths will be collection of paths (final answer)
    def dfs(self, root, path, paths):
        path += str(root.val)
        print(path)
        # base case; when we reach leaf with no children
        # OR there are no more paths
        # when reaching one we will at it to paths

        if root.left is None and root.right is None:
            paths.append(path)
            return
        
        if root.left is not None:
            self.dfs(root.left, path + '->', paths)
        
        if root.right is not None:
            self.dfs(root.right, path + '->', paths)

#testing
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.left.left = TreeNode(4)

print(tree.binaryTreePaths(tree))
        