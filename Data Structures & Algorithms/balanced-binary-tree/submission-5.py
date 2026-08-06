# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(root):
            if not root: 
                return (True, 0)

            left_balanced, left_height = getHeight(root.left)
            right_balanced, right_height = getHeight(root.right)
            
            cur_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            cur_height = 1 + max(left_height, right_height)

            return (cur_balanced, cur_height)
        
        return getHeight(root)[0]
        

        
            
            

        