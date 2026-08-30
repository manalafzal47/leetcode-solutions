# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # create a queue and res
        queue = deque([root])
        res = []

        # have a while loop that rightside and qlen
        while queue:
            qlen=len(queue) #length of each level 
            rightside = None

        # have a for loop that runs if not null then update rightside.
            for i in range(qlen): # check each level
                node = queue.popleft()

                # taken every node in the level, and added to the queue. 
                # removed all elements from last level and added the level 
                if node:
                    rightside=node  # will have rightside of the level
                    queue.append(node.left)
                    queue.append(node.right)

    # after traversing the level, add the most rightside val to the res array
            if rightside:
                res.append(rightside.val)
                # take rightside and append that to a value
        return res

