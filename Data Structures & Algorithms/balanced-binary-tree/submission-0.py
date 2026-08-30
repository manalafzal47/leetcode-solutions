# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced means that the abs value between the left - right > 1

        balanced = [True]

        # check for if both left and right subtrees dont have >1 difference betwene L and R trees
        def height(root):

            # edge case:
            if root is None:
                return 0

            left_subtree=height(root.left)
            right_subtree=height(root.right)

            if abs(left_subtree-right_subtree) > 1:
                balanced[0]=False
                return 0

            return 1+max(left_subtree,right_subtree)
        
        height(root)
        return balanced[0]
                    


    




