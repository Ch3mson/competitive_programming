"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        output = []
        ptr = root
        while ptr:
            output.append(ptr.val)
            ptr = ptr.next
        
        return output