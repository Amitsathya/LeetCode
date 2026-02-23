# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy2 = left = ListNode()
        dummy = right = ListNode()
        curr = head
        while curr:
            if curr.val < x:
                left.next = ListNode(curr.val)
                left = left.next
            else:
                right.next = ListNode(curr.val)
                right = right.next
            curr = curr.next
        left.next = dummy.next
        return dummy2.next