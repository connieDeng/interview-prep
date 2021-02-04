# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return
        
        q = []
        q.append(root)

        while(len(q) != 0):
            curr = []
            n = len(q)

            # if node has children
            while n > 0:
                # queue pop front
                p = q[0]
                q.pop(0)
                # curr.append(p)

                for i in range(len(p.children)):
                    q.append(p.children[i])
                n -= 1
        print('\n')

        

# testing code
root = Node(1)
root.children.append(Node(3))
root.children.append(Node(2))
root.children.append(Node(3))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))

self.levelOrder(root)