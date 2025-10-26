# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(k, groupPrev)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next



    def getKth(self, k, l):
        while l and k:
            l = l.next
            k -= 1
        return l
