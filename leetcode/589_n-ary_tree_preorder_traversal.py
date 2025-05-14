"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []


        def dfs(node, output):
            if not node: return
            output.append(node.val)
            for n in node.children:
                dfs(n, output)
        
        dfs(root, output)
        return output
