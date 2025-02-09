# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.output = float('inf')
        self.last = float('-inf')

        def dfs(root):
            if not root: return
            if root.left:
                dfs(root.left)
            if abs(root.val - self.last) < self.output:
                self.output = abs(root.val - self.last)
            self.last = root.val
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return self.output