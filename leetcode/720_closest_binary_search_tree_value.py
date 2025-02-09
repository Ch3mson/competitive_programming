# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.output = root.val

        def dfs(node):
            if not node: return
            if abs(target - node.val) == abs(target - self.output):
                self.output = min(node.val, self.output)
            if abs(target - node.val) < abs(target - self.output):
                self.output = node.val
            if target < node.val:
                dfs(node.left)
            if target > node.val:
                dfs(node.right)

        dfs(root)
        return self.output