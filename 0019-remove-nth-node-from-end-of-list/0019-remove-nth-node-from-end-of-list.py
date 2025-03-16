# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        second = node
        fast = head
        while n:
            fast =fast.next
            n -= 1
        while fast:
            fast = fast.next
            second = second.next
        second.next = second.next.next
        return node.next
        