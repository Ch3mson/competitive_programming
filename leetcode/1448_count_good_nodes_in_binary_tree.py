# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0

        def dfs(root, currMax):
            if not root: return
            if root.val >= currMax:
                self.output += 1
            newMax = max(currMax, root.val)
            left = dfs(root.left, newMax)
            right = dfs(root.right, newMax)

        dfs(root, root.val)
        return self.output