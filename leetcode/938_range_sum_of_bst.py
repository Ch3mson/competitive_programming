# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def bfs(root, low, high):
            if not root: return 0
            output = 0
            if root.val <= high and root.val >= low:
                output += root.val
            left_sum = bfs()
            return bfs(root.left, low, high) + bfs(root.right, low, high)
        
        return bfs(root, low, high)