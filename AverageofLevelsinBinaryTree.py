# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
       # implement a BFS (FIFO): first in first out; Queue
        ans = []
        if root == None:
           return ans
        
        queue = []
        # if root node exists add it to queue
        queue.append(root)

        while queue:
            size = len(queue)
            sum = 0
            for i in range(size):
                #FIFO
                current_node = queue.pop(0)
                sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            ans.append(float(sum/size))
        print(ans)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()

        

#testing
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

tree.averageOfLevels(tree)

"""
Comments
- keeping decimal points by casting both values to floats
- BFS using queues
"""