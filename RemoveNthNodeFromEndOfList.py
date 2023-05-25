# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        val = head
        counter = 0
        updated_counter = n
        while val:
            counter += 1
            val = val.next
        updated_counter = counter - n
        node = head
        previous = ListNode(0)
        while updated_counter > 0:
            previous = node
            node = node.next
            updated_counter -= 1
        if node == head:
            return head.next
        previous.next = node.next
        return head