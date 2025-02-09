# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        output = []
        q.append(root)
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if i == qLen - 1:
                        output.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return output