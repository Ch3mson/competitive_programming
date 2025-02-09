# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        front = head
        temp = head
        while front:
            temp = front.next
            front.next = prev
            prev = front
            front = temp
        
        return prev