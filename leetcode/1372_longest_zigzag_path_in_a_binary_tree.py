# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(root, goLeft, steps):
            if root:
                self.output = max(self.output, steps)
                if goLeft:
                    dfs(root.left, False, steps + 1)
                    dfs(root.right, True, 1)
                else:
                    dfs(root.left, False, 1)
                    dfs(root.right, True, steps + 1)
        dfs(root, True, 0)
        return self.output