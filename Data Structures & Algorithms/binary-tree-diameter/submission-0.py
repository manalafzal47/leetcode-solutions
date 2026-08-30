# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # note: that the diameter refers to the longest diameter in the tree , 
        # and that means the left and right heights added from the root.
        
        # define dfs function that calculates left and right heights, and returns heights 
        # checks for the longest diameter and returns that length 

        longestDiameter=[0]

        # create a height function that returns the height of that root
        def height(root):
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            diameter = left+right

            longestDiameter[0]=max(longestDiameter[0], diameter)

            return 1+max(left, right)
        
        height(root)
        return longestDiameter[0]



        # Time complexity: 0(n)

        # space complexity: 0(h) --> dfs will always be height, because it vertical space.


            