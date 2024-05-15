# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find the "left" node
        prevLeft, cur = dummy, head
        for i in range(left - 1):
            prevLeft = cur
            cur = cur.next

        # reverse
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # update pointers
        prevLeft.next.next = cur
        prevLeft.next = prev
        return dummy.next