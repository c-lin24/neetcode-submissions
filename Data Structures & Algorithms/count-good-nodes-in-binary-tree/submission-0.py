# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0

        def dfs(node, maxPast):
            if not node:
                return 0
            if node.val >= maxPast:
                good = 1
            else: 
                good = 0
            
            maxi = max(maxPast, node.val)
            right = dfs(node.right, maxi)
            left = dfs(node.left, maxi)

            return left + right + good

        return dfs(root, root.val)           
