# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        counts = defaultdict(int)
        q.append(root)

        while q:
            curr = q.pop()
            counts[curr.val] += 1
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        maxCount = max(counts.values())
        output = []
        for k, v in counts.items():
            if v == maxCount:
                output.append(k)
        
        return output
