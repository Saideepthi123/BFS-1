# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# tc : O(n) # traversing each node
# sc : O(1) # out array space is not considers ad extra space so O(1)
# intution : each level the nodes are basically the childs of the root, so wil use a queue ( so that i can extract fifo)
# the size of the queue tells us the number of nodes in that level will use this paramter to pop the nodes and save them in a list 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = deque()
        q.append(root) 
        ans = []

        if root is None:
            return ans

        while q:
            level = []
            n = len(q) # number of nodes in that level 
            for i in range(n):
                node = q.popleft() # fifo
                level.append(node.val) # added the nodes in the ith level 

                if node.left is not None: # add its respective child nodes in the queue 
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            ans.append(level) # saving each level nodes in the list 

        return ans




        