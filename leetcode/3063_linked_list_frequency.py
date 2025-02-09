# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = defaultdict(int)

        ptr = head
        while ptr:
            counts[ptr.val] += 1
            ptr = ptr.next
        
        
        dummy = ListNode()
        ptr = dummy

        for val, freq in counts.items():
            ptr.next = ListNode(freq)
            ptr = ptr.next
        
        return dummy.next