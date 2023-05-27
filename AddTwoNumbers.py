# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = ListNode(0)
        curr_pointer = val
        sum = 0
        carry = 0
        while l1 or l2 or carry > 0:
            if l1:
                updated_l1 = l1.val
            else:
                updated_l1 = 0
            if l2:
                updated_l2 = l2.val
            else:
                updated_l2 = 0
            sum = updated_l1 + updated_l2 + carry
            carry = sum // 10
            sum = sum % 10
            curr_pointer.next = ListNode(sum)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr_pointer = curr_pointer.next
        return val.next


