class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        # always do an edge case
        if root == None:
            return result
        # BFS uses a queue data structure

        queue = []
        queue.append(root)
        # while queue is not empty
        while(queue):
            # get size of queue
            size = len(queue)
            currentLevel = []
            # for loop to process queue
            for i in range(size):
                # pop first element because we are doing a BFS
                # queueu FIFO
                current = queue.pop(0)
                currentLevel.append(current.val)
                
                # check if left or right children exist
                # if exist put into queue to get processes
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right) 
            result.append(currentLevel)
        return result

#testing 
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.right = TreeNode(7)
tree.right.left = TreeNode(15)

print(tree.levelOrder(tree))
        