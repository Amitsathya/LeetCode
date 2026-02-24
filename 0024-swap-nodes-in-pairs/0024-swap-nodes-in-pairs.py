# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leftPrev = dummy = ListNode(0, head)
        curr = head
        while curr and curr.next:
            prev = None
            for _ in range(2):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            leftPrev.next.next = curr
            temp2 = leftPrev.next
            leftPrev.next = prev
            leftPrev = temp2
        return dummy.next