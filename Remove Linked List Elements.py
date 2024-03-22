# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # insert dummy point right before head
        dummy = ListNode(next=head)
        prev, cur = dummy, head

        while cur:
            temp = cur.next

            if cur.val == val:
                prev.next = temp
            else:
                prev = cur
            cur = cur.next
        return dummy.next